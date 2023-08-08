class Solution:
    def numberOfWays(self, s: str) -> int:
        memo = {
            "0":0, "1":0, "01":0, "10":0, "101":0, "010":0
        }
        for num in s:
            if num == "0":
                memo["0"] += 1
                memo["10"] += memo["1"]
                memo["010"] += memo["01"]
            elif num == "1":
                memo["1"] += 1
                memo["01"] += memo["0"]
                memo["101"] += memo["10"]
        return memo["101"] + memo["010"]
        
        
        
        
        
        """
        hsh_mp = {0:[i for i in range(len(s)) if s[i] == '0'],
                  1:[j for j in range(len(s)) if s[j] == '1']}
        #print(hsh_mp)
        res = 0
        for x in [0,1]:
            n = len(hsh_mp[x])
            for i in range(1, n):
                    res += ((hsh_mp[x][i] - hsh_mp[x][i-1])- 1) * i * (n - i)

        return res
        """