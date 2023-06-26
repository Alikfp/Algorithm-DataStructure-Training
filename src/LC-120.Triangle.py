class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = triangle[0]
        i = 1
        while i < len(triangle):
            nxt_memo = []
            for j, x in enumerate(triangle[i]):
                if j == 0: nxt_memo.append(x+memo[0])
                elif (j == i): nxt_memo.append(x+memo[-1])
                else:
                    nxt_memo.append(min(x+memo[j], x+memo[j-1]))
            memo = nxt_memo
            i += 1
        return min(memo)