class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        # make memo
        memo = [-1 for _ in range(amount+1)]
        memo[0] = 0
        # fill memo array
        for i in range(len(memo)):
            #print(i, memo)
            poss = []
            for c in coins:
                if i-c >= 0 and memo[i-c] >= 0:
                    poss.append(memo[i-c])
            #print(poss)
            if poss:
                memo[i] = min(poss)+1
        
        # return the result
        return memo.pop()