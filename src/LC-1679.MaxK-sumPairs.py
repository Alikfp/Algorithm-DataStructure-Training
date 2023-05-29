class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sort the array
        arr = sorted(nums)
        l, r = 0, len(nums)-1
        op_count = 0
        # init 2 pointers at the end of start of the array
        while r > l:
            if arr[l] + arr[r] > k:
                r -= 1
                continue
            elif arr[l] + arr[r] < k:
                l += 1
                continue
            else:
                op_count += 1
                l += 1
                r -= 1
        
        return op_count