# Holy this is hard
# Idea is you need to use prefix sum and find a subarray which has the same remainder as the total sum

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        remainder = {0: -1}
        cur = 0
        res = n = len(nums) #set to highest value possible

        for index , value in enumerate(nums):
            cur = (cur + value) % p
            remainder[cur] = index # stores rightmost index
            if (cur - need) % p in remainder: # Find another number with the required remainder
                res = min(res, index - remainder[(cur - need) % p])
        
        return res if res < n else -1

# Taken from leetcode solutions
