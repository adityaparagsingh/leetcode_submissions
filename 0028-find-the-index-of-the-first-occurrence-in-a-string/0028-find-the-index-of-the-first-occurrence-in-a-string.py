class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        if needle in haystack:
            ans = haystack.find(needle,0)
            
        return ans