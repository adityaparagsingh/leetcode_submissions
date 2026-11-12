class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        asc = desc = max_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                asc += 1
            else:
                asc = 1

            if nums[i] < nums[i-1]:
                desc += 1
            else:
                desc = 1

            max_len = max(max_len, asc, desc)

        return max_len