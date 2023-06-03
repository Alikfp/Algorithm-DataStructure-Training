class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while hi > lo:
            mid = (lo + hi) // 2
            # valley after mid
            if nums[mid] > nums[hi]:
                lo = mid + 1
            
            # valley before mid
            elif nums[mid] <= nums[hi]:
                hi = mid
        
        return nums[hi]