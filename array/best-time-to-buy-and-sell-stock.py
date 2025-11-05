class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        currentDip = prices[0]
        for price in prices:
            if price < currentDip:
                currentDip = price
            else:
                profit = price - currentDip
                maxProfit = max(maxProfit, profit)
        return maxProfit
        