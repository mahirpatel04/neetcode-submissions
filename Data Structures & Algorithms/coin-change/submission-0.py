class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        dp[0] = 0

        for i in range(1, len(dp)):
            minWays = float("inf")
            for c in coins:
                if c > i:
                    continue
                
                minWays = min(minWays, dp[i - c] + 1)

            dp[i] = minWays

        return dp[amount] if dp[amount] != float("inf") else - 1