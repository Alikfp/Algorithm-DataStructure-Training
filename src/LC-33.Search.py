class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, end = 0, len(nums)-1
        
        while st <= end: 

            mid = (st + end) // 2
            #print(st, mid, end)
            if target == nums[mid]:
                return mid

            # case after mid
            if nums[mid] >= nums[st]:

                if target > nums[mid]:
                    st = mid + 1
                
                elif target < nums[mid]:

                    if nums[end] > nums[mid] or nums[st] <= target : # a
                        end = mid - 1
                    else: # b
                        st = mid + 1

            # case before mid
            else: # mid < st
                if target < nums[mid]:
                    end = mid - 1
                
                elif target > nums[mid]:
                    if nums[end] < target : # a
                        end = mid - 1
                    else: # b
                        st = mid + 1
        return -1



