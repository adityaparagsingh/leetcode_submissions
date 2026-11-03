class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minmoves = 0
        for num in nums:
            minmoves+= (max(nums)-num)
        return minmoves