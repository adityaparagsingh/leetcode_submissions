class Solution:
    def findMin(self, nums: list[int]) -> int:
        # return min(nums)
        n = len(nums)
        l = 0 
        r = n-1
        while l<r:
            m = l + ((r-l)//2)
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m
        return nums[l]