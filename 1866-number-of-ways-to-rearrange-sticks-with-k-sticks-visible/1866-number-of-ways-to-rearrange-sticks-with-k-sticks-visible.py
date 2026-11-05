class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize a DP table
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Base case: 1 way to arrange 0 sticks with 0 visible sticks
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):  # Number of sticks considered
            for j in range(1, min(i, k) + 1):  # Number of visible sticks
                # Case 1: Current stick is visible
                dp[i][j] = dp[i - 1][j - 1] % MOD  # Previous sticks, one less visible
                
                # Case 2: Current stick is not visible
                dp[i][j] += (i - 1) * dp[i - 1][j] % MOD  # Previous sticks, same visible count
                dp[i][j] %= MOD  # Ensure we stay within MOD

        # Return the number of arrangements for n sticks with exactly k visible
        return dp[n][k]
