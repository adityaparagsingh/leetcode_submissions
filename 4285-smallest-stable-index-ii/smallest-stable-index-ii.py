class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefixMax = [nums[0]] * n
        suffixMin = [nums[-1]] * n
        for i in range(1,n):
            prefixMax[i] = max(prefixMax[i-1],nums[i])
        for i in range(n-2,-1,-1):
            suffixMin[i] = min(suffixMin[i+1],nums[i])
        for i in range(n):
            if prefixMax[i]-suffixMin[i] <= k:
                return i
        return -1