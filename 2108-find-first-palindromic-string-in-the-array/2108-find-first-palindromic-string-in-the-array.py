class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for ch in words:
            l = 0
            r = len(ch)-1
            while ch[l]==ch[r]:
                if l>=r:
                    return ch
                l+=1
                r-=1
        return ""