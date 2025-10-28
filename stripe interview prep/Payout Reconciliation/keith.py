# When Stripe pays out to a merchant, each charge belongs to a transfer group.
# Sometimes a payout might miss or double-count charges — your job is to detect mismatches.

# You receive two lists of charges for a given transfer group:
# expected: the charges that should be included in the payout

import os

def solve():
    base_dir = os.path.dirname(__file__)
    input_file = os.path.join(base_dir, 'input1.txt')
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        expected = {}

        for _ in range(n):
            line = f.readline().strip()
            charge_id, group_id, amount = line.split(',')
            expected[group_id] = expected.get(group_id, 0) + int(amount)
        
        m = int(f.readline().strip())
        actual = {}
        for _ in range(m):
            line = f.readline().strip()
            payout_id, group_id, amount = line.split(',')
            actual[group_id] = actual.get(group_id, 0) + int(amount)
    
        all_groups = sorted(set(expected.keys()).union(set(actual.keys())))
        print("REPORT")
        for group_id in all_groups:
            exp_amount = expected.get(group_id, 0)
            act_amount = actual.get(group_id, 0)
            diff = act_amount - exp_amount
            if diff == 0:
                status = "MATCH"
            elif diff > 0:
                status = "EXTRA_PAYOUT"
            else:
                status = "MISSING_PAYOUT"
            print(f"{group_id} {status} {exp_amount} {act_amount}")
solve()