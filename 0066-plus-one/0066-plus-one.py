class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        r = n-1
        while r>=0:
            if len(set(digits)) == 1 and digits[0] == 9:
                arr = [0]*(n+1)
                arr[0]=1
                return arr
            if digits[r] != 9:
                digits[r] += 1
                break
            else:
                digits[r] = 0
                r -= 1

        return digits