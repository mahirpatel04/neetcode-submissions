class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1

        profit = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                currProf = prices[s] - prices[b]
                profit = max(currProf, profit)
            else:
                b = s
            
            s += 1

        return profit
