class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1: return n
        res = i = 0
        while i <= n - k:
            for d in (k, k + 1):
                if i + d <= n and s[i : i + d] == s[i : i + d][::-1]:
                    res += 1
                    i += d
                    break
            else:
                i += 1
        return res
        # count = 0
        # i = 0
        # while i <=len(s) - k:
        #     found = False
        #     for j in range(len(s),i+k-1,-1):
        #         str1 = s[i:j]
        #         if str1 == str1[::-1]:
        #             count +=1
        #             i = j
        #             found = True 
        #             break
        #     if not found:
        #         i+=1
        # return count
        # for i in range(len(s)):
        #     str1 = s[i:i+3]
        #     if str1 == str1[::-1] and len(str1)<=3:
        #         count+=1
        # return count