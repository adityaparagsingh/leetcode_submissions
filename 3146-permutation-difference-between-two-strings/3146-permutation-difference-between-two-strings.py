class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        for i in s:
            x = abs(t.index(i) - s.index(i))
            ans+=x
        return ans