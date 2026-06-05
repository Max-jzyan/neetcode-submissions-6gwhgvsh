class Solution:
    def climbStairs(self, n: int) -> int:
        # DP, bottom up
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        # dp[2] = 11, 02
        # dp[3] = 111,21,12
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
            # dp[i-1]
            # dp[i-2]
        return dp[n]
