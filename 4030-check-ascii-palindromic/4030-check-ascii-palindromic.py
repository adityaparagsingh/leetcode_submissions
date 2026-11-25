class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary = ''.join(format(ord(c), '08b') for c in s)
        if binary == binary[::-1]:
            return True
        return False