class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, mx_sum, curr_mx, mn_sum, cur_mn = 0, nums[0], 0, nums[0], 0

        for num in nums:
            curr_mx = max(curr_mx + num, num)
            mx_sum = max(mx_sum, curr_mx)
            cur_mn = min(cur_mn+num, num)
            mn_sum = min(mn_sum, cur_mn)
            total += num

        return max(mx_sum, total-mn_sum) if mx_sum > 0 else mx_sum


