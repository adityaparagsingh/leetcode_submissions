class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            n = str(num)
            ans = 0
            for digit in n:
                ans+=int(digit)
            num = ans
        return num