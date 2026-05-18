class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 101
        profit = 0

        for index in range(len(prices)):
            if prices[index] <= buy:
                buy = prices[index]
            else:
                profit = max(profit, prices[index] - buy)
        
        return profit
        