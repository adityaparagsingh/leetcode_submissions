class Solution:
    def maxDepth(self, s: str) -> int:
        r = 0 
        depth = 0 
        for char in s:
            if char == ')':
                depth -=1
                continue
            if char != '(':
                continue
            depth +=1
            if depth>r:
                r = depth
        return r
        # maxcounter = 0 
        # counter = 0 
        # for i in range(len(s)):
        #     if s[i]=='(':
        #         counter+=1
        #     elif s[i]==')':
        #         counter-=1
        #     maxcounter = max(maxcounter,counter)
        # return maxcounter