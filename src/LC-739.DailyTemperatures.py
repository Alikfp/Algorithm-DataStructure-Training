from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque([])
        res = [0 for _ in temperatures]
        for i, curr in enumerate(temperatures):
            # Curr is larger than our min, pop till for all j, temp[stack[j]] < curr
            while stack and curr > temperatures[stack[-1]]:
                s = stack.pop()
                res[s] = i - s
            # We have a new smallest
            else:
                stack.append(i)
        return res