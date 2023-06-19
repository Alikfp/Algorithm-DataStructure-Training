from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == '.': continue

                sqr, sqc = r//3, c//3
                sqi = sqr*3 + sqc
                if curr in row_set[r] or \
                   curr in col_set[c] or \
                   curr in square_set[sqi]:
                   return False

                row_set[r].add(curr)
                col_set[c].add(curr)
                square_set[sqi].add(curr)

        return True