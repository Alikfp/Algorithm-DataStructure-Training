class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [1 for _ in range(len(s))]
        if s[0] == '0':
            return 0

        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] in ['1', '2']:
                    memo[i] = memo[i-2]
                else:
                    return 0
            else:
                if (s[i-1] == '1') or (s[i-1] == '2' and int(s[i]) < 7):
                    memo[i] = memo[i-2] + memo[i-1]
                else:
                    memo[i] = memo[i-1]

        return memo[-1]