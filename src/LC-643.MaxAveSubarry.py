class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        _sum = curr
        l, r = 1, k
        while r < len(nums):
            #print(l, r)
            #print(_sum)
            curr += (nums[r]-nums[l-1])
            _sum = max(_sum, curr)
            l, r = l+1, r+1
            
        return _sum/k