class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # ans = 0

        # for i in range (len(arr1)):
        #     flag = True
        #     for j in range (len(arr2)):
        #         if abs(arr1[i]-arr2[j]) <= d:
        #             flag = False            
        #             break
        #     if flag == True:
        #         ans+=1
        # return ans
        count=0
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    count+=1
                    break
        return len(arr1)-count