class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            buy_price, sell_price = prices[buy], prices[sell]
            profit = sell_price - buy_price
            if profit <= 0:
                buy = sell
                sell = buy
            elif profit > max_profit:
                max_profit = profit
            sell += 1
        return max_profit