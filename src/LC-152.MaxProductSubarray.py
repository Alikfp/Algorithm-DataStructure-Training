class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn, mx = 1, 1
        ans = nums[0]

        for num in nums:
            vals = [num*mn, num*mx, num]
            mn, mx = min(vals), max(vals)

            ans = max(mx, ans)
        
        return ans