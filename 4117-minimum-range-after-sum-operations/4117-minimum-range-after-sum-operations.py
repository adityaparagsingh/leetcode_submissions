class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        min1,min2,max1 = sorted([a,b,c])
        return min(max1-min1, min2)