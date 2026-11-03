class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minmoves = 0
        m = max(nums)
        for num in nums:
            minmoves+= (m-num)
        return minmoves