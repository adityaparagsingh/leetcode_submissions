class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        sum = 0
        for i in range(len(s)):
            sum += int(s[i])
        return sum