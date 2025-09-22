# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        mini = [0]*l
        maxi = [0]*l

        mini[0] = prices[0]
        for i in range(l-1):
            mini[i+1] = min(mini[i], prices[i+1])

        maxi[l-1] = prices[l-1]
        for i in range(l - 2, -1, -1):
            maxi[i] = max(prices[i], maxi[i+1])

        diff = [0]*l
        p=0

        for i in range (0,l-1):
            diff[i] = max(0, maxi[i]-mini[i])
            p = max(p, diff[i])
        return p