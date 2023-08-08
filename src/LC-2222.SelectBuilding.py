class Solution:
    def numberOfWays(self, s: str) -> int:
        hsh_mp = {0:[i for i in range(len(s)) if s[i] == '0'],
                  1:[j for j in range(len(s)) if s[j] == '1']}
        #print(hsh_mp)
        res = 0
        for x in [0,1]:
            n = len(hsh_mp[x])
            for i in range(1, n):
                    res += ((hsh_mp[x][i] - hsh_mp[x][i-1])- 1) * i * (n - i)

        return res
