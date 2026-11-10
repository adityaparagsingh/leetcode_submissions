class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower():
            l, r = 0, len(nums)
            while l < r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid
            return l

        def upper():
            l, r = 0, len(nums)
            while l < r:
                mid = (l+r)//2
                if nums[mid] <= target:
                    l = mid+1
                else:
                    r = mid
            return l

        first = lower()

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        return [first, upper()-1]