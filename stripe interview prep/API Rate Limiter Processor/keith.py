# Stripe’s infrastructure throttles client requests based on rate limits.
# Your job is to process an API request log and determine, for each client, which requests succeeded and which were throttled.

import os

def solve():
    base_dir = os.path.dirname(__file__)
    input_file = os.path.join(base_dir, 'input1.txt')
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        client_requests = {}

        for _ in range(n):
            line = f.readline().strip() # 0 A /v1/charges
            timestamp, client_id, endpoint = line.split(' ')
            if client_id not in client_requests:
                client_requests[client_id] = []
            client_requests[client_id].append(int(timestamp))
            client_requests[client_id].sort()
            # Keep only the timestamps within the last 10 seconds
            while client_requests[client_id] and client_requests[client_id][0] < int(timestamp) - 10:
                client_requests[client_id].pop(0)
            
            if len(client_requests[client_id]) > 3:
                print(f"{timestamp} {client_id} {endpoint} THROTTLED")
            else:
                print(f"{timestamp} {client_id} {endpoint} OK")


solve()