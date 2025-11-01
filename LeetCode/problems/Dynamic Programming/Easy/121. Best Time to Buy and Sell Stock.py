class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## solution 2: Time O(N); Space O(1)
        max_profit = 0
        min_p = prices[0]
        for p in prices[1:]:
            max_profit = max(p-min_p, max_profit)
            min_p = min(min_p, p)
        return max_profit
        
        # ## solution 1: Reverse Time O(N); Space O(1)
        # out = 0
        # c = -1
        # for p in range(len(prices)-2,-1,-1):
        #     out = max(prices[c]-prices[p], out)
        #     c = p if prices[p]>prices[c] else c
        # return out
