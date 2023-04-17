class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def perm(curr, rem):
            if len(rem) == 0:
                res.append(curr)
                return
            for i in rem:
                perm(curr + [i], rem - set([i]))
        
        perm([], set(nums))
        return res