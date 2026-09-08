class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = sorted(s)
        tt = sorted(t)
        for i in range(len(ss)):
            if ss[i]!=tt[i]:
                return tt[i]
        return tt[-1]