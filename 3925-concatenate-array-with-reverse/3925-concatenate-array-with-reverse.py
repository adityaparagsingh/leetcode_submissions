class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = nums+nums[::-1]
        return ans