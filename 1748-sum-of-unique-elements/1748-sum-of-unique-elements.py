from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        sum = 0
        for key,val in c.items():
            if val == 1:
                sum +=key
        return sum