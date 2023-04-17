class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cands = sorted(candidates)

        def dfs(rem, stack):       
            if rem == 0:
                res.append(stack)
            for c in cands:
                if rem < 0:
                    break
                elif stack and c < stack[-1]:
                    continue
                else:
                    dfs(rem-c, stack + [c])
        
        dfs(target, [])
        return res