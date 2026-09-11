class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # n = len(digits)
        # r = 3
        # count = 0
        # ans = 0
        # for i in range(r):
        #     ans += n-1
        # if len(str(ans)) == 3 and ans%2 == 0:
        #     count+=1
        # return count
        nums = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and j!=k and i!=k:
                        if digits[i] != 0 and digits[k]%2 == 0:
                            num = digits[i] * 100 + digits[j] * 10 + digits[k]
                            nums.add(num)
        return len(nums)