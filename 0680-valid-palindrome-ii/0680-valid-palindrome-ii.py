# from collections import Counter
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # count = Counter(s)
        # if len(s)!=1:
        #     for val in count.values():
        #         if val%2==0:
        #             return True
        #     return False
        # else:
        #     return True
        def isPal(i,j):   #2 Pointer approach
            while i<j:
                if s[i]!=s[j]:
                    return False
                i,j = i+1,j-1
            return True 
        i,j = 0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return isPal(i+1,j) or isPal(i,j-1)
            i,j = i+1,j-1
        return True