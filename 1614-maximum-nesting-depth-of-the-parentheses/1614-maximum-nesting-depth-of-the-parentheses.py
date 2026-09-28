class Solution:
    def maxDepth(self, s: str) -> int:
        maxcounter = 0 
        counter = 0 
        for i in range(len(s)):
            if s[i]=='(':
                counter+=1
            elif s[i]==')':
                counter-=1
            maxcounter = max(maxcounter,counter)
        return maxcounter