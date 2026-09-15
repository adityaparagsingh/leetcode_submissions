class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        i = 0
        while i<(len(s)-1):
            score+=abs(ord(s[i])-ord(s[i+1]))
            i+=1
        # for i in range(len(s)):
        #     score+=abs(ord(s[i])-ord(s[i+1]))
        return score