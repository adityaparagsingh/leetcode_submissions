class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        sum = []
        for i in range(len(nums)):
            x = x+nums[i]
            sum.append(x)
        return sum