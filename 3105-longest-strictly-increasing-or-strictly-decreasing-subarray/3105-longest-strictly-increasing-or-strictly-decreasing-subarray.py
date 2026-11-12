class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = 1

        for i in range(len(nums)):
            asc = desc = 1

            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    asc += 1
                    desc = 1
                elif nums[j] < nums[j-1]:
                    desc += 1
                    asc = 1
                else:
                    break

                max_len = max(max_len, asc, desc)

        return max_len