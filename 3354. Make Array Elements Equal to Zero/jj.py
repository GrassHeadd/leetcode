class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        print(prefix)

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]
        print(suffix)

        for i, num in enumerate(nums):
            if num == 0:
                print("called")
                if abs(suffix[i] - prefix[i]) == 0:
                    ans += 2
                elif abs(suffix[i] - prefix[i]) == 1:
                    ans += 1

        return ans
