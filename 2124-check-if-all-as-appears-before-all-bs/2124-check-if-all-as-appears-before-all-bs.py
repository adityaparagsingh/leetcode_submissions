class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(1,len(s)):
            if s[i-1] =='b' and s[i]=='a':
                return False
        return True