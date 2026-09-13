class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        countarr = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i!=j and nums[j]<nums[i]:
                    count+=1
            countarr.append(count)
        return countarr