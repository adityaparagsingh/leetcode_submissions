class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = str(nums[i])
            sum = 0
            for j in range(len(s)):
                sum+=int(s[j])
            if sum == i:
                return i
        return -1