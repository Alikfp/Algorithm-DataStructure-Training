class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0

        for i, num in enumerate(nums):
            furthest = max(num+i, furthest)
            #print(furthest)
            if furthest >= len(nums)-1:
                return True

            if i == furthest:
                return False