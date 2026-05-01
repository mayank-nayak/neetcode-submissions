class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxiProfit = 0
        minPrice = prices[0]
        for price in prices:
            maxiProfit = max(maxiProfit, price - minPrice)
            minPrice = min(minPrice, price)
        return maxiProfit