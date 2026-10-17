class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        minprice=prices[0]
        for i in range(1, len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            elif prices[i]-minprice>profit:
                profit=prices[i]-minprice
        return profit

        
        
        