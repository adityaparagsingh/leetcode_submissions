class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        #two pointer approach
        left = 0
        right = len(nums)-1
        str = []
        while left<=right:
            if abs(nums[left])<abs(nums[right]):
                str.append((nums[right])**2)
                right-=1
            else:
                str.append((nums[left])**2)
                left+=1
        str.reverse()
        return str