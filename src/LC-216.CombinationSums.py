class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs (rem_k, target, acc):
            if rem_k == 0 and target == 0:
                res.append(acc)
            else:
                for num in range(acc[-1]+1, 10):
                    if target - num >= 0:
                        dfs(rem_k-1, target-num, acc + [num])
        

        for num in range(1, 10):
            if num <= n:
                dfs(k-1, n-num, [num])
        
        return res