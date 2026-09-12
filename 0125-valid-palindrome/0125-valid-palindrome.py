class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = s.lower()
        newstr = ""
        for i in str1:
            if i.isalnum():
                newstr += i
        if newstr==newstr[ : :-1]:
            return True
        return False