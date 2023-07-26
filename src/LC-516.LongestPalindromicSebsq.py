class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_rev = s[::-1]
        n = len(s)
        memo = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1, n+1):
                if s[i-1] == s_rev[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        return memo[n][n]
                    