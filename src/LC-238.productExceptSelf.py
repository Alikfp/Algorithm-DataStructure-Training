class Solution:
    def productExceptSelf(self, nums):
        # fill pref and suff
        n = len(nums)
        pref= [1 for _ in range(n)]
        suff =[1 for _ in range(n)]

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        for j in range(n-1, 0, -1):
            suff[j-1] = suff[j] * nums[j]

        return [p*s for p,s in zip(pref, suff)]