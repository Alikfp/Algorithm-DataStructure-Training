class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            if (i < 0) or (i >= m) or (j < 0) or (j >= n) or board[i][j]!="O":
                return
            board[i][j] = "S"
            children = [(i-1, j), (i+1, j),
                        (i, j-1), (i, j+1)]
            for x, y in children:
                dfs(x, y)
        
        m, n = len(board), len(board[0])
        for r in range(m):
            dfs(r, 0)
            dfs(r, n-1)
        for c in range(n):
            dfs(0, c)
            dfs(m-1, c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"