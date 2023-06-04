class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Bianry search
        m = len(matrix)
        n = len(matrix[0])
        lo, hi = 0, m*n

        if m == 1 and n == 1:
            return matrix[0][0] == target

        # pointer logic
        def pointer_pos(ind):
            return max(0,((ind-1)) //n), (max(0,(ind-1)) % n)

        while hi >= lo:
            mid = (lo + hi) // 2
            mid_i, mid_j = pointer_pos(mid)

            if matrix[mid_i][mid_j] < target:
                lo = mid + 1

            elif matrix[mid_i][mid_j] > target:
                hi = mid - 1
            
            else:
                return True
        
        return False