# class Solution:
#     def countDigitOne(self, n: int) -> int:
#         count = 0
#         for num in range(n+1):
#             if '1' in str(num):
#                 # count+=1
#                 count += str(num).count('1')
#         return count 
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1

        while i <= n:
            q = n // i
            r = n % i

            count += (q + 8) // 10 * i
            if q % 10 == 1:
                count += r + 1

            i *= 10

        return count