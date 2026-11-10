# class Solution:
#     def climbStairs(self, n: int, costs: list[int]) -> int:
#         costs = [0] + costs  # step 0 is free, step i costs costs[i]

#         @cache
#         def climb(i: int = 0) -> int:  # cheapest way from i to n
#             if i > n:
#                 return inf  # jumped past the top
#             if i == n:
#                 return costs[n]  # on top: just pay for it
#             return costs[i] + min(climb(i + 1) + 1, climb(i + 2) + 4, climb(i + 3) + 9)

#         return climb()
class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        costs = [0] + costs
        dp = [inf] * (n + 3)  # dp[i] = climb(i), the two steps past the top stay inf
        dp[n] = costs[n]
        for i in reversed(range(n)):  # from the top step down
            dp[i] = costs[i] + min(dp[i + 1] + 1, dp[i + 2] + 4, dp[i + 3] + 9)
        return dp[0]