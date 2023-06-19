class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #if len(nums) == 1: return 0
        nums = [-float("inf")] + nums + [-float("inf")]
        lo, hi = 0, len(nums)-1
        while hi >= lo:
            mid = (lo+hi)//2
            if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
                return mid-1
            elif (nums[mid] > nums[mid-1]) and (nums[mid] < nums[mid+1]):
                lo = mid
            else:
                hi = mid





        #dif = 1
        #for i, num in enumerate(nums):
        #    nxt_dif = nums[i]-nums[i-1] if i != 0 else 1
        #    if (dif * nxt_dif) < 0:
        #        return i-1
        #    dif = nxt_dif
        
        #return len(nums)-1