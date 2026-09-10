class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        arr = []
        sum2 = 0
        sum1 = 0
        for num in nums:
            sum1+=num
            for digit in str(num):
                arr.append(int(digit))
        for a in arr:
            sum2+=a
        return abs(sum2-sum1)