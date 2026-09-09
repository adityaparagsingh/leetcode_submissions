class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            unique = True
            for j in range(len(s)):
                if i!= j and s[i]==s[j]:
                    unique = False
                    break
            if unique:
                return i
                    # return i
                    # break
        return -1