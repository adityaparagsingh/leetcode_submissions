class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        count = 0
        i = 0 
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                count+=1
                i+=1
            else:
                i+=1
        return count