from common_imports import *
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp_f(x, y):
            if x + y > y + x: # Concetenate string
                return 1
            elif x == y:
                return 0
            else:
                return -1
        
        nums = [str(num) for num in nums]

        nums.sort(key = cmp_to_key(cmp_f), reverse = True)

        return ''.join(nums).lstrip('0') or '0'