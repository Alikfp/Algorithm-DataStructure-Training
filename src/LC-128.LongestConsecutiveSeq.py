class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        mx_streak = 0

        for st in nums_set:
            if st-1 in nums_set:
                continue
            else:
                seq_len = 1
                end = st + 1
                while end in nums_set:
                    seq_len += 1
                    end += 1
                mx_streak = max(mx_streak, seq_len)
        return mx_streak

        
        
        
        #hshmap = dict()
        #lngst_srs = 0
        #for num in nums:
        #    if num in hshmap: continue
        #    left = hshmap[num-1] if num-1 in hshmap else 0
        #    right = hshmap[num+1] if num+1 in hshmap else 0
        #    hshmap[num] = None
        #    curr_len = left+right+1
        #    hshmap[num-left] = curr_len
        #    hshmap[num+right] = curr_len
        #    lngst_srs = max(lngst_srs, curr_len)
        #return lngst_srs


