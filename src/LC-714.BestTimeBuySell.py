class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bought = -prices[0]
        sold = 0

        for p in prices:
            bought = max(bought, sold-p)
            sold = max(sold, bought+p-fee)
        return sold
        
