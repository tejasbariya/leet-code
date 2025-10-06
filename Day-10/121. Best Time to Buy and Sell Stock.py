class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = [0]
        price = prices[0]
        for i in range(len(prices)):
            curr_profit = prices[i] - price
            profit.append(curr_profit)
            if prices[i] < price:
                price = prices[i]
        return max(profit)