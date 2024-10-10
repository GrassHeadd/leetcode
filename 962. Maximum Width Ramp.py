class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i) # Stores the index of a decreasing stack
        
        for j in range(len(nums) -1, -1, -1): # Start from the back, initial, end, step
            while stack and nums[j] >= nums[stack[-1]]:
                res = max(j - stack.pop(), res)
        
        return res