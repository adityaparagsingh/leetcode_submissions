class Solution:
    def singleNumber(self, nums):
        n = len(nums)
        nums.sort()
        for i in range(0, n - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[n - 1]
