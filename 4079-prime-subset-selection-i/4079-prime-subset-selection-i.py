class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n<2:
            return []

        is_prime = [True]*(n+1)
        is_prime[0] = is_prime[1] = False

        for i in range(2,int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,n+1,i):
                    is_prime[j]=False
                    
        ans = []
        total = 0
        
        for num in range(2,n+1):
            if is_prime[num]:
                if total + num<=s:
                    ans.append(num)
                    total+=num
                else:
                    break
        return ans
        #     prime = True
            
        #     for i in range(2,int(num**0.5)+1):
        #         if num%i==0:
        #             prime = False
        #             break
            
        #     if prime and total + num <= s:
        #         ans.append(num)
        #         total +=num
        # return ans
        
        
        
        
        # ans = []
        # for i in range(len(prime)):
        #     if total + prime[i] < s:
        #         break
        #     ans.append(prime[i])
        #     total+=prime[i]