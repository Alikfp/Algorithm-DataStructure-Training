class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        l, r = 0, nums[0]
        jumps = 1
        while r <= len(nums)-1:
            jumps += 1
            nxt_bound = max([nums[i]+i for i in range(l, r+1)])
            l, r = r, nxt_bound
        return jumps