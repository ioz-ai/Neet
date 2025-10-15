# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the same day. Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any time.

# Find and return the maximum profit you can achieve.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
            
        max_profit = 0
        
        # Iterate from the second day (index 1) to the end
        for i in range(1, len(prices)):
            # Calculate the difference between today's price and yesterday's price
            daily_gain = prices[i] - prices[i-1]
            
            # If there is any profit, add it to the total.
            # This is equivalent to summing all "valleys to peaks."
            if daily_gain > 0:
                max_profit += daily_gain
                
        return max_profit