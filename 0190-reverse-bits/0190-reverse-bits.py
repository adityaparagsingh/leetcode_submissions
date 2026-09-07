class Solution:
    def reverseBits(self, n: int) -> int:
        num1 = format(n,'032b')
        # num2 = int(str(num1)[::-1],2)
        return int(str(num1)[::-1],2)