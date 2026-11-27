class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        return (
            [x for x in nums if x < pivot]+
            [x for x in nums if x == pivot]+
            [x for x in nums if x > pivot]
        )