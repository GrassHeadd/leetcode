# Problem: Idempotency-Key Stream Processor

# Stripe APIs rely on idempotency keys to ensure retries don’t create duplicate charges.
# You’ll process a stream of POST attempts and decide which ones actually take effect.

# Rules

# You receive N lines of events. Each event is two fields:

# an idempotency_key (ASCII, no spaces),

# a body (the raw JSON payload as a string, may contain spaces).

# Process events top-to-bottom:

# If a new key appears → ACCEPT and remember the body for that key.

# If the key has appeared with the exact same body string → IGNORE (duplicate).

# If the key has appeared with a different body string → CONFLICT (do not accept).

# Equality of bodies is exact string equality (no JSON parsing/normalization).

import os

def solve():
    base_dir = os.path.dirname(__file__)
    input_file = os.path.join(base_dir, 'input1.txt')
    print(f"Reading from {input_file}")
    with open(input_file, 'r') as f:
        seen = {}
        accepted_body = []
        conflict_keys = []
        n = int(f.readline().strip())

        for _ in range(0, n):
            line = f.readline()  # a {"amt":10,"cur":"USD"}
            if not line:
                break
            line = line.rstrip('\n')
            split = line.find(' ')
            if split == -1:
                key = line
                body = ""
            else:
                key = line[0: split]
                body = line[split + 1:]
            
            if key not in seen:
                seen[key] = body
                accepted_body.append(body)
            else:
                if seen[key] == body:
                    continue
                else:
                    conflict_keys.append(key)
            
    print("ACCEPTED")
    for body in accepted_body:
        print(body)
    print("CONFLICT")
    for key in conflict_keys:
        print(key)
    

if __name__ == "__main__":
    solve()