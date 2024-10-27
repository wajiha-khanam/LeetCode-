class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy
        r = 1 # sell
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                Profit = prices[r] - prices[l]
                maxP = max(maxP, Profit)
            else:
                l = r
            r += 1
        return maxP


