class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)

        while h > l:
            mid = (l + h) // 2
            if nums[mid] >= target:
                h = mid
            elif nums[mid] < target:
                l = mid+1
        
        return h