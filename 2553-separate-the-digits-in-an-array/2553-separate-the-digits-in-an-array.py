class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            for digit in str(num):
                arr.append(int(digit))
        return arr