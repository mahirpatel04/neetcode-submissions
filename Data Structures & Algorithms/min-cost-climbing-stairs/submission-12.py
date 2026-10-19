class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        elif len(cost) <= 2:
            return min(cost)

        
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])