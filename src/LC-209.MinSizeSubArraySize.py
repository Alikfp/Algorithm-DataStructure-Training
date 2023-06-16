class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r, l = 0, 0
        acc = 0
        min_suba_len = float('inf')
        while r < len(nums):
            acc += nums[r]
            while acc >= target:
                min_suba_len = min(min_suba_len, r-l+1)
                acc -= nums[l]
                l += 1
            r += 1
        return min_suba_len if min_suba_len != float('inf') else 0