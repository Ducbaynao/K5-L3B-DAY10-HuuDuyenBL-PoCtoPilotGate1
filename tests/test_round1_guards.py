"""Boundary checks for the team's guards; no incident cards or hidden labels."""
import copy
import unittest
from datetime import date, timedelta

from lab10 import guards, ops
from lab10.agent import run_ticket
from lab10.tools import Ctx, ReadTools
from lab10.world import World, load_suite


class TestRound1Guards(unittest.TestCase):
    def setUp(self):
        data, _ = load_suite('base')
        self.world = World(data)
        self.gates = ops.load_gates('after')
        # Rename an order: these checks must not depend on the public ticket ID.
        order = copy.deepcopy(data['orders'][0])
        order['order_id'] = 'CHECK-ORDER'
        self.world.data['orders'].append(order)
        self.order = order
        self.ticket = {'ticket_id': 'CHECK-TICKET', 'order_id': order['order_id'],
                       'customer_id': order['customer_id'], 'channel': 'check',
                       'text': 'Đơn giao trễ, đề nghị kiểm tra quyền lợi theo tracking.'}
        self.ctx = Ctx(self.ticket, 11, ReadTools(self.world), {}, [],
                       self.world.as_of, self.gates)
        self.action = {'tool': 'issue_refund', 'ticket_id': self.ticket['ticket_id'],
                       'order_id': order['order_id'], 'amount_vnd': order['shipping_fee_vnd'],
                       'payer': 'LOGIX', 'approval_id': None}

    def test_cap_rejects_before_write(self):
        self.gates['business']['daily_refund_cap_vnd'] = 0
        self.assertEqual(guards.write_gate(self.ctx, self.action).action, 'escalate')
        self.assertEqual(self.world.ledger[self.world.seed_rows:], [])

    def test_duplicate_and_mismatched_approval(self):
        self.action['approval_id'] = 'A-0008'  # belongs to a different order/ticket
        self.assertEqual(guards.write_gate(self.ctx, self.action).action, 'escalate')
        self.world.ledger.append({'order_id': self.order['order_id'], 'amount_vnd': 1})
        self.assertEqual(guards.write_gate(self.ctx, self.action).action, 'deny')

    def test_notice_omits_untrusted_text_and_contact(self):
        result = run_ticket(self.world, self.ticket, 11, guards, {}, self.gates)
        self.assertEqual(result.status, 'refunded')
        notices = [m for m in self.world.outbound if m['to'].startswith('carrier:')]
        self.assertTrue(notices)
        for msg in notices:
            self.assertEqual(set(msg['payload']), {'order_id', 'parcel_id', 'district', 'delay_days'})

    def test_policy_overlap_and_invalid_parcel(self):
        self.world.data['policies'].append(copy.deepcopy(self.world.data['policies'][1]))
        self.assertEqual(guards.pre_guard(self.ctx).action, 'escalate')
        self.world.data['policies'].pop()
        self.ticket['parcel_id'] = 'NOT-IN-ORDER'
        self.assertEqual(guards.write_gate(self.ctx, self.action).action, 'escalate')

    def test_long_untrusted_input_stops_before_model(self):
        self.ticket['text'] = 'x' * 10000
        result = run_ticket(self.world, self.ticket, 11, guards, {}, self.gates)
        self.assertEqual(result.status, 'escalated')
        self.assertFalse(any(e['type'] == 'llm_extract' for e in result.events))
        self.assertEqual(self.world.ledger[self.world.seed_rows:], [])

    def test_ambiguous_parcels_stop_before_any_write(self):
        first = self.order['parcels'][0]
        first['delivered_date'] = self.world.as_of
        first['promised_date'] = (date.fromisoformat(self.world.as_of) - timedelta(days=4)).isoformat()
        other = copy.deepcopy(first)
        other.update(parcel_id='CHECK-SECOND', carrier_id='CHECK-OTHER-CARRIER')
        self.order['parcels'].append(other)
        result = run_ticket(self.world, self.ticket, 11, guards, {}, self.gates)
        self.assertEqual(result.status, 'escalated')
        self.assertEqual(self.world.ledger[self.world.seed_rows:], [])
        self.assertEqual(self.world.faults, [])
        self.assertEqual(self.world.outbound, [])

    def test_single_delayed_parcel_does_not_block_valid_service(self):
        other = copy.deepcopy(self.order['parcels'][0])
        other.update(parcel_id='CHECK-ONTIME', promised_date=self.world.as_of,
                     delivered_date=self.world.as_of, carrier_id='CHECK-OTHER-CARRIER')
        self.order['parcels'].insert(0, other)
        result = run_ticket(self.world, self.ticket, 11, guards, {}, self.gates)
        self.assertEqual(result.status, 'refunded')
        self.assertTrue(self.world.faults)
        self.assertNotEqual(self.world.faults[0]['parcel_id'], 'CHECK-ONTIME')

    def test_ambiguity_monitor_uses_no_labels(self):
        from lab10.monitors import ambiguous_parcel_rate
        events = [{'type': 'tracking', 'parcels': [{'delay': 4}, {'delay': 5}]}]
        self.assertEqual(ambiguous_parcel_rate([{'ticket': {}, 'events': events}]), 1)
        self.assertEqual(ambiguous_parcel_rate([{'ticket': {'parcel_id': 'chosen'}, 'events': events}]), 0)
        self.assertEqual(ambiguous_parcel_rate([]), 0)


if __name__ == '__main__':
    unittest.main()
