# import math
class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        # nums = [0]*n
        # nums[index] = value
        if value == 1:
            if index>0 or n-index >1:
                return -1
            return 1

        p = value
        for i in range(2,int(value**0.5)+1):
            if value % i == 0 :
                p=i
                break
        if index > (value - p) //2:
            return -1
        steps = n - index -1

        if steps == 0 :
            return value
            
        return value + p+2 *(steps-1)