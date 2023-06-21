class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            pv = nums[len(nums)//2]
            l, m, r = [], [], []
            for x in nums:
                if x > pv:
                    r.append(x)
                elif x < pv:
                    l.append(x)
                else:
                    m.append(x)
            i, j = len(l), (len(l)+len(m))
            if k <= i:
                return helper(l, k)
            elif k > j:
                return helper(r, k-j)
            else:
                return pv
        return helper(nums, len(nums)-k+1)
