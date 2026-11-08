class Solution:
    def countValidSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        a = 0

        for i in range(n):
            if i>=2 and s[i-2:i+1] == 'abc':
                a = i-1

            count += (i-a+1)
        
        # i , abc = 0,0
        # while i <= n-3:
        #     if s[i:i+3] =="abc":
        #         abc +=1
        return count
        