class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxElement = max(nums)
        minElement = min(nums)
        ans = []
        for i in range(minElement,maxElement):
            if i not in nums:
                ans.append(i)
        return ans