class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        while nums and len(res) < 2:
            num = nums.pop()
            if num in nums:
                res.append(num)
        return res