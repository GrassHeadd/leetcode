class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        ans = 0
        while True:
            if n >= (2**x):
                ans += 2**x
                x += 1
            else:
                return ans
