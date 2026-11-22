class Solution:
    def minCost(self, nums: list[int]) -> int:
        mid = sorted(nums[1:-1])
        extra = sum(
            mid[i]+mid[i+1]
            for i in range(0,len(mid)-1,2)
            if mid[i] + mid[i+1]<0
        )
        return nums[0] + nums[-1] + extra
        