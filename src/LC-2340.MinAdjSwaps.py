class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        mx_i, mx = None, -float('inf')
        mn_i, mn = None, float('inf')
        for i in range(len(nums)):
            if nums[i] >= mx:
                mx = nums[i]
                mx_i = i
            if nums[i] < mn:
                mn = nums[i]
                mn_i = i

        return mn_i + (len(nums)-(mx_i+1)) - (mx_i < mn_i)