class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        arr = []
        # ans = float('inf')
        for i in range(0,len(nums),2):
            num = int(str(nums[i])+str(nums[i+1]))
            # ans = min(ans,num)
            arr.append(int(num))
        return min(arr)