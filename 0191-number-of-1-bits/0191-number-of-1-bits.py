class Solution:
    def hammingWeight(self, n: int) -> int:
        num = format(n,'04b')
        str1 = list(str(num))
        # for i in range(len(str1)):
        #     if str1[i] == '0':
        #         str1.pop(i)
        #         # str1.replace("0",'')
        i = 0
        while i < len(str1):
            if str1[i] == '0':
                str1.pop(i)
            else:
                i+=1
        return len(str1)