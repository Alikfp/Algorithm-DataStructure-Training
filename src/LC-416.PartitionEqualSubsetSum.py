class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False

        # memo array
        memo = [[False if s != 0 else True for s in range((sum_ // 2)+1)] for _ in nums]
        mx_sum = 0
        for i in range(len(memo)):
            for s in range(1, len(memo[0])):
                fst_pos = snd_pos = False
                if i-1 >= 0:
                    fst_pos = memo[i-1][s]
                    if s - nums[i] >= 0:
                        snd_pos = memo[i-1][s - nums[i]]
                
                memo[i][s] = fst_pos | snd_pos


        return memo[-1][-1]