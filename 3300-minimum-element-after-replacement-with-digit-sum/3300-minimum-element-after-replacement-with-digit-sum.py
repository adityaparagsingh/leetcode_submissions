class Solution:
    def minElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # minarr =[]
        # for num in nums:
        #     sum = 0
        #     while num > 0:
        #         sum += num % 10
        #         num //= 10
        #     minarr.append(sum)
        # return min(minarr)
        n=len(nums)
        for i in range(n):
            s=0
            for j in str(nums[i]):
                s+=int(j)
            nums[i]=s
        return min(nums)       
        