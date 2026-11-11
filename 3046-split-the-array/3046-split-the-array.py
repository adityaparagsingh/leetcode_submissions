class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n1=[]
        n2=[]
        for  i in nums:
            if i  not in n1:
                n1.append(i)
            elif i  not in n2:
                n2.append(i)
            else:
                return False
                break
        return True