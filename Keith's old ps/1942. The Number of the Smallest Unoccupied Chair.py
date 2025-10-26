class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len (times)

        arrivals = [(times[i][0], i) for i in range(n)]
        arrivals.sort()

        availableChairs = list(range(n)) #min-heap to track available chairs
        heapq.heapify(availableChairs)

        leavingQueue = []

        for arrivalTime, friendIndex in arrivals:
            # Free chairs with leaving time before current arrival time
            while leavingQueue and leavingQueue[0][0] <= arrivalTime:
                heapq.heappush(availableChairs, heapq.heappop(leavingQueue)[1])

            chair = heapq.heappop(availableChairs) # Assign smallest chair

            if friendIndex == targetFriend:
                return chair
            
            # Mark chair as used until friend leave
            heapq.heappush(leavingQueue, (times[friendIndex][1], chair))

        return -1