class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        total = 0
        for num in s:
            total += int(num)
        if x%total == 0:
            return total
        return -1