class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_memo = [[1 if (row == m-1) or (col == n-1) else None \
                      for col in range(n)] for row in range(m)]

        def calc_paths(i, j):
            #print(i, j)
            #print(path_memo)
            if path_memo[i][j] is not None:
                return path_memo[i][j]
            elif i >= m or j >= n:
                return 0
            else:
                path_memo[i][j] = calc_paths(i, j+1) + calc_paths(i+1, j)
                return path_memo[i][j]

        calc_paths (0,0)
        return path_memo[0][0]