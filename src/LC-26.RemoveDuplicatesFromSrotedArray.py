class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lgst_n_ind = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[lgst_n_ind]:
                lgst_n_ind += 1
                nums[lgst_n_ind] = nums[i]

        return lgst_n_ind+1