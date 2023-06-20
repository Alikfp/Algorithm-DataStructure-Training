class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_fut = prices[-1]
        mx_prof = 0
        
        for i in range(len(prices)-2, -1, -1):
            mx_prof = max(mx_prof, mx_fut - prices[i])
            mx_fut = max(mx_fut, prices[i])

        return mx_prof
