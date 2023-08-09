from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sub_hsh = Counter(nums[:k])
        curr_sum = sum(sub_hsh)
        mx_sum = curr_sum if len(sub_hsh)==k else 0

        for i in range(k, len(nums)):
            
            if nums[i] in sub_hsh:
                sub_hsh[nums[i]] += 1
            else: 
                sub_hsh[nums[i]] = 1
                curr_sum += nums[i]
            if sub_hsh[nums[i-k]] > 1:
                sub_hsh[nums[i-k]] -= 1
            else: 
                del sub_hsh[nums[i-k]]
                curr_sum -= nums[i-k]
            #print(sub_hsh)
            #print(curr_sum)
            if len(sub_hsh) == k:
                mx_sum = max(mx_sum, curr_sum)
        
        return mx_sum




