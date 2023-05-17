class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[float('inf') for _ in grid[0]] for _ in grid]
        memo[-1][-1] = grid[-1][-1]
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                #print(memo)
                d, r = float('inf'), float('inf')
                if i < len(grid)-1 :
                    d = memo[i+1][j]
                if j < len(grid[0])-1 :
                    r = memo[i][j+1]
                if d == float('inf') and r == float('inf'):
                    memo[i][j] = grid[i][j]
                else:
                    memo[i][j] = grid[i][j] + min(d, r)
        
        return memo[0][0]
