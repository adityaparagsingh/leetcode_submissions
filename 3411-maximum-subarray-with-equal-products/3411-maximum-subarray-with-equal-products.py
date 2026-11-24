from math import gcd, lcm, prod

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        maxlen = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub = nums[i:j+1]

                if prod(sub) == lcm(*sub) * gcd(*sub):
                    maxlen = max(maxlen, len(sub))

        return maxlen
