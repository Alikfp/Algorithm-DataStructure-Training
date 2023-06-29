class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        pref_sums = {0:1}
        res = 0
        for num in nums:
            total += num
            if total - k in pref_sums:
                res += pref_sums[total - k ]
            if total in pref_sums:
                pref_sums[total] += 1
            else:
                pref_sums[total] = 1
        return res