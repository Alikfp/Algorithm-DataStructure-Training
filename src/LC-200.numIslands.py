class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find and sink
        m = len(grid)
        n = len(grid[0])
        def sink(i,j):
            #print(grid)
            if (0 <= i < m) and (0 <= j < n) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0

        return sum(sink(i,j) for i in range(m) for j in range(n))