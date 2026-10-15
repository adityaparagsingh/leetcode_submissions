class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            seen = set()
            for j in range(i,len(nums)):
                seen.add(nums[j])
                length = len(seen)
                ans += length**2
            
        return ans