from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        i = 0
        j = 0
        while i < len(nums):
            #print(c)
            while c[j] < 1:
                j += 1

            nums[i] = j
            c[j] -= 1
            i += 1