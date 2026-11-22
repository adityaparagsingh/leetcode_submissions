class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for num in nums1:
            if num in nums2:
                ans.append(num)
                nums2.remove(num)
        return ans