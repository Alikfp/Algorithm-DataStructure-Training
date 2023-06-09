class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for i in range(2, len(nums)):
            if nums[i] > nums[slow-1]:
                slow += 1
                nums[slow] = nums[i]

        return slow + 1