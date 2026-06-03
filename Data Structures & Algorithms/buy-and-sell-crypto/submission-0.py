class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7, 9, 1, 2
        # Two pointer
        l = 0 # l is buy, i is sell
        maxProfit = 0
        for i, v in enumerate(prices):
            if v < prices[l]:
                l = i
                continue
            p = v - prices[l]
            if p > maxProfit:
                maxProfit = p
        return maxProfit
            