class Solution:
    def numSquares(self, n: int) -> int:
        memo = [float('inf') for _ in range(n+1)]
        memo[0], memo[1] = 0, 1
        sqs = []
        i = 1
        while i*i <= n:
            sqs.append(i*i)
            i += 1
        for num in range(2, n+1):
            options = [memo[num-sq] if num>=sq else float('inf') for sq in sqs]
            memo[num] = min(options)+1
        return memo[-1]