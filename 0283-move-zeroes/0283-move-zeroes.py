class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = (len(nums)-1)
        k=0      #two pointer i,k
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1

        while k<len(nums):
            nums[k]=0
            k+=1
            # if nums[i]==0:
            #     nums.pop(i)
            #     nums.append(0)
        return