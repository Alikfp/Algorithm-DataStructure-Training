class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0, 0]
        for h in nums:
            curr_best = max(h+memo[0], memo[1])
            memo = [memo[1], curr_best]
        return memo[1]
