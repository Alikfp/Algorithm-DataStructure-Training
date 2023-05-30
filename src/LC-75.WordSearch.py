class Solution:
    def dfs(self, r, c, i, board, word):
        #print(board)
        m, n = len(board), len(board[0]) 
        # whether next char of our target existis in this substring
        if (r < 0) or (r > m-1) or (c < 0) or (c > n-1) or (board[r][c] != word[i]):
            return False

        if (board[r][c] == word[i]) and (i == len(word)-1):
            return True
        
        tmp = board[r][c]
        board[r][c] = "$"
        adjs = self.dfs(r+1, c , i+1, board, word) or self.dfs(r-1, c , i+1, board, word) or \
                self.dfs(r, c-1 , i+1, board, word) or self.dfs(r, c+1 , i+1, board, word)
        board[r][c] = tmp
        return adjs

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0]) 
        for r in range(m):
            for c in range(n):
                if self.dfs(r, c, 0, board, word):
                    return True
        return False
        