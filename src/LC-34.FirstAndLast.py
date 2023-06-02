class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search_l (t):
            lo, hi = 0, len(nums)
            while hi > lo:
                mid = (lo + hi) // 2
                if nums[mid] < t:
                    lo = mid + 1
                elif nums[mid] >= t:
                    hi = mid
            return lo
        
        l = search_l(target)
        return [l, search_l(target+1)-1] if target in nums[l:l+1] else [-1, -1]
