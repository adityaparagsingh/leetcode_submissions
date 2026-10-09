class Solution:
    def trap(self, height: List[int]) -> int:

        l_height = r_height = 0
        n = len(height)
        prefixArr = [0]*n
        suffixArr = [0]*n

        for i in range (n):
            j = -i-1     #starts at -1
            prefixArr[i] = l_height
            suffixArr[j] = r_height
            l_height = max(l_height,height[i])
            r_height = max(r_height,height[j])

        water = 0
        for i in range (n):
            potential = min(prefixArr[i],suffixArr[i])
            water += max(0,potential-height[i])
        
        return water
        