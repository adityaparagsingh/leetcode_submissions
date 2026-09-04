class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            left = nums[: i + 1]
            right = nums[i:]
            if max(left) - min(right) <= k:
                return i
        return -1
