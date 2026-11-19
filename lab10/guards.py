"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Vòng 1 kiểm chính sách theo ngày, quyền ghi tiền, trách nhiệm hãng và payload gửi đi.
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    try:
        day = H.d(ctx.as_of)
        policies = [p for p in ctx.tools.lookup_policies()
                    if H.d(p['effective_from']) <= day
                    and (not p.get('effective_to') or day <= H.d(p['effective_to']))]
    except (KeyError, TypeError, ValueError):
        return Verdict.escalate('không xác minh được ngày hiệu lực chính sách')
    if len(policies) != 1:
        return Verdict.escalate('cần đúng một chính sách hiệu lực')
    # Reserve the worst normal path: two policy checks, confirmation and decision note.
    prices = ctx.tools.ops_facts().get('llm_cost', {})
    order = ctx.tools.lookup_order(ctx.ticket.get('order_id')) or {}
    texts = [ctx.ticket.get('text', '')]
    if order.get('checkout_note'):
        texts.append(order['checkout_note'])
    projected = ctx.cost_vnd + sum(prices.get('extract_base_vnd', 0)
                                  + len(text) // 4 * prices.get('extract_per_4_chars_vnd', 0)
                                  for text in texts)
    projected += 2 * prices.get('policy_check_vnd', 0) + prices.get('confirm_vnd', 0)
    if ctx.gates.get('operations', {}).get('decision_note'):
        projected += prices.get('decision_note_vnd', 0)
    ceilings = [ctx.tools.ops_limits().get('max_llm_cost_per_ticket_vnd'),
                ctx.gates.get('business', {}).get('cost_budget_per_ticket_vnd')]
    if any(limit is not None and projected > limit for limit in ceilings):
        return Verdict.escalate('dự toán vượt ngân sách xử lý ticket; chuyển người trước khi gọi model')
    return Verdict.allow(policy_id=policies[0]['policy_id'])


def write_gate(ctx, action):
    tool = action.get('tool')
    if tool == 'send_reply':
        return Verdict.allow()
    if tool not in ('issue_refund', 'file_carrier_fault', 'notify_carrier'):
        return Verdict.deny('thao tác ghi chưa được cho phép')
    order = ctx.tools.lookup_order(ctx.ticket.get('order_id'))
    if not order or order.get('customer_id') != ctx.ticket.get('customer_id'):
        return Verdict.escalate('không xác minh được chủ đơn')
    try:
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if not policy or not order.get('parcels'):
            return Verdict.escalate('thiếu chính sách hoặc tracking')
        if ctx.ticket.get('parcel_id') and not any(
                p['parcel_id'] == ctx.ticket['parcel_id'] for p in order['parcels']):
            return Verdict.escalate('kiện không thuộc đơn')
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        entitlement = H.entitlement_vnd(policy, order, delay, parcel.get('delay_cause'))
    except (KeyError, TypeError, ValueError):
        return Verdict.escalate('dữ liệu nghiệp vụ thiếu hoặc không hợp lệ')
    if tool in ('issue_refund', 'file_carrier_fault') and action.get('order_id') != order['order_id']:
        return Verdict.escalate('lệnh ghi không khớp đơn đã xác minh')

    if tool == 'issue_refund':
        if ctx.tools.ledger_rows(order_id=order['order_id']):
            return Verdict.deny('đơn đã có khoản hoàn trong sổ cái; không ghi lần hai')
        if entitlement <= 0:
            return Verdict.deny('tracking và chính sách không cho phép hoàn')
        if not parcel.get('delay_cause'):
            return Verdict.escalate('chưa có nguyên nhân trễ được ghi nhận')
        if action.get('payer', 'LOGIX') != 'LOGIX' or action.get('amount_vnd') != entitlement:
            return Verdict.escalate('số tiền hoặc bên trả khác quyền lợi đã xác minh')
        approval_id = action.get('approval_id')
        if approval_id:
            approvals = ctx.tools.lookup_approvals(approval_id=approval_id)
            approval = approvals[0] if len(approvals) == 1 else {}
            try:
                valid = (approval.get('status') == 'valid'
                         and approval.get('ticket_id') == ctx.ticket['ticket_id']
                         and approval.get('order_id') == order['order_id']
                         and approval.get('customer_id') == order['customer_id']
                         and approval.get('approver_id') == (ctx.gates.get('operations', {}).get('approver_id') or 'NV-HANH')
                         and approval.get('max_vnd', 0) >= entitlement
                         and H.d(approval['expires_at']) >= H.d(ctx.as_of)
                         and not ctx.tools.ledger_rows(approval_id=approval_id))
            except (KeyError, TypeError, ValueError):
                valid = False
            if not valid:
                return Verdict.escalate('phê duyệt không hợp lệ hoặc đã sử dụng')
        else:
            limits = ctx.tools.ops_limits()
            if entitlement > policy['auto_limit_vnd']:
                return Verdict.escalate('vượt hạn mức tự động, cần phê duyệt hợp lệ')
            customer_total = sum(r['amount_vnd'] for r in ctx.tools.ledger_rows(customer_id=order['customer_id'])
                                 if not r.get('approval_id'))
            if customer_total + entitlement > limits.get('max_auto_refund_per_customer_per_day_vnd', 300000):
                return Verdict.escalate('vượt trần tự động theo khách; cần người duyệt')
            caps = [limits.get('daily_auto_refund_budget_vnd'),
                    ctx.gates.get('business', {}).get('daily_refund_cap_vnd')]
            if any(cap is not None and ctx.tools.auto_refund_today_vnd() + entitlement > cap for cap in caps):
                return Verdict.escalate('vượt trần hoàn tự động trong ngày')

    if tool == 'file_carrier_fault':
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny('tracking không đủ điều kiện quy lỗi cho hãng')
        if ctx.tools.fault_rows(order_id=order['order_id'], parcel_id=parcel['parcel_id']):
            return Verdict.deny('kiện đã có lỗi hãng, không ghi trùng')
        if len(ctx.tools.fault_rows(carrier_id=parcel['carrier_id'])) >= ctx.tools.ops_limits().get('max_auto_strikes_per_carrier_per_day', 2):
            return Verdict.deny('đạt trần lỗi hãng tự động; cần đối soát người duyệt')
        return Verdict.modify('quy trách nhiệm theo tracking từng kiện', parcel_id=parcel['parcel_id'],
                              carrier_id=parcel['carrier_id'], driver_id=parcel.get('driver_id'), delay_days=delay)

    if tool == 'notify_carrier':
        if action.get('carrier_id') != parcel['carrier_id'] or not ctx.tools.fault_rows(
                order_id=order['order_id'], parcel_id=parcel['parcel_id'], carrier_id=parcel['carrier_id']):
            return Verdict.deny('không gửi thông báo khi chưa xác minh trách nhiệm hãng')
        safe = {'order_id': order['order_id'], 'parcel_id': parcel['parcel_id'],
                'district': order['recipient']['district'], 'delay_days': delay}
        allowed = set(policy['carrier_notice_fields'])
        return Verdict.modify('chỉ gửi dữ liệu nghiệp vụ theo policy; bỏ ghi chú và thông tin liên hệ',
                              payload={k: v for k, v in safe.items() if k in allowed})
    return Verdict.allow()
