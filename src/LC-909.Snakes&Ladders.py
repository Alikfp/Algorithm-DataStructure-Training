class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        final = (n*n)
        board = board[::-1]
        def get_cell (x):
            q, r = x//n, x%n
            if q % 2 == 0:
                return q, r
            else:
                return q, (n-1)-r
        
        # bfs
        move_count = 0
        q = deque([0])
        visited = set()
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                i, j = get_cell(curr)
                if board[i][j] != -1: curr = board[i][j]-1
                if (curr+1) == final: return move_count
                for move in range(1, 7):
                    nxt = min(final-1, curr + move)
                    if (nxt not in visited):
                        visited.add(nxt)
                        q.append(nxt)
            move_count += 1
        
        return -1
        