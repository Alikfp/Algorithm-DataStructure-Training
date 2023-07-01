class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[w], nums[i] = nums[i], nums[w]
                w += 1
        return nums