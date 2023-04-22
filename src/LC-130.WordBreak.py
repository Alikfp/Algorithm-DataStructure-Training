class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [True] + [False for _ in s]

        for i in range(len(s)):
            for word in wordDict:
                #print(memo)
                st = i - len(word) + 1
                #print(word, s[st:i+1])
                #print('before', st, memo[st - 1])
                if memo[st] and s[st:i+1] == word:
                    memo[i+1] = True
        
        return memo[-1]