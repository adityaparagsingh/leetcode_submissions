class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower():
            l = 0
            r = len(nums)
            while l<r:
                m = (l+r)//2
                if nums[m]<target:
                    l = m+1
                else:
                    r = m
            return l
        
        first = lower()
        
        def upper():
            l = 0
            r = len(nums)
            while l<r:
                m = (l+r)//2
                if nums[m]<=target:
                    l = m+1
                else:
                    r = m
            return l
        if first == len(nums) or nums[lower()]!= target:
            return [-1,-1]
        return (lower(),upper()-1)