class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i , n in enumerate(nums):
            if n == target:
                return i
        return -1