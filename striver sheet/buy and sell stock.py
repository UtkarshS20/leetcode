from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = float('inf') 
        for i in range(n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, (prices[i] - min_price))
            # for j in range(i+1, n):
                # if prices[j]>prices[i]:
                #     if max_profit < (prices[j]-prices[i]):
                #         max_profit = prices[j]-prices[i]
        return max_profit
                
max_value = Solution()
prices = [7,1,5,3,6,4]
print(max_value.maxProfit(prices=prices))