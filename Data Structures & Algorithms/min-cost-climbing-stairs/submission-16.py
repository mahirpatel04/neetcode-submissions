class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        elif len(cost) <= 2:
            return min(cost)

        
        dp = [0] * len(cost)
        # cost for the first 2 stairs is simply cost of those stairs
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            # Pick the smaller cost of the previous 2 and add the cost of the current stair
            dp[i] = min(dp[i-1], dp[i - 2]) + cost[i]

        # return the smaller cost of the last two stairs
        return min(dp[-1], dp[-2])