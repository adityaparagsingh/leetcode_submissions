class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = []
        n = len(nums)
        for i in range(n):
            if n%(i+1)!=0:
                continue
            else:
                #special number
                ans.append(nums[i]*nums[i])
        return sum(ans)