class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ops_count = 0
        while r > l:
            if nums[l] > nums[r]:
                nums[r-1] += nums[r]
                r -= 1
                ops_count += 1
            elif nums[l] < nums[r]:
                nums[l+1] += nums[l]
                l += 1
                ops_count += 1
            else:
                l += 1
                r -= 1
        
        return ops_count