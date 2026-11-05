class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        # arr.sort()
        
        # if len(arr)<=2: 
        #     return True
        # for i in range(len(arr)-2):
        #     if len(arr)>2 and ((arr[i] - arr[i+1]) != (arr[i+1] - arr[i+2])):
        #         return False
        # return True

        arr.sort()  
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False

        return True