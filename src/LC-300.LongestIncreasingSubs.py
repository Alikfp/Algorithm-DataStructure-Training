class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = [nums[0]]
        for num in nums:
            #print("subs", subs)
            if num > subs[-1]:
                subs.append(num)
            else:
                # Binary search
                lo, hi = 0, len(subs)-1
                while hi > lo:
                    m = (hi+lo)//2
                    if subs[m] < num:
                        lo = m+1
                    else:
                        hi = m
                subs[hi] = num

        return len(subs)