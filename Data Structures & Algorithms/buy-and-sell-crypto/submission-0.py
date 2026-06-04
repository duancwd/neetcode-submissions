class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        l = len(prices) - 1
        sell = 1
        profit = 0


        while sell <= l:
            if prices[sell] >= prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])


            else:
                buy = sell

            sell +=1





        return profit 