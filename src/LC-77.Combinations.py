class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(curr, i, rem):
            if rem == 0:
                #print(res)
                res.append(curr)
            else:
                for num in range(i, n+1):
                    helper(curr + [num], num+1, rem-1)
        
        helper([], 1, k)
        #print(res)
        return res