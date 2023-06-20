class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot_prof = 0
        for i in range(1, len(prices)):
            delta = max(0, prices[i] - prices[i-1])
            tot_prof += delta
        
        return tot_prof