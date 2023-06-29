class Solution:
    def candy(self, ratings: List[int]) -> int:
        memo = [1 for _ in ratings]
        n = len(ratings)

        # left scan
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                memo[i] = max(memo[i], memo[i-1]+1)
        # right scan
        for i in range(n-2, -1, -1):
            if (ratings[i] > ratings[i+1]):
                memo[i] = max(memo[i],memo[i+1]+1)
            
        return sum(memo)