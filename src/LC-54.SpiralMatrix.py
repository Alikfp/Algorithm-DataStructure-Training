class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # define bounds
        m, n = len(matrix), len(matrix[0])
        t, b = -1, m
        l, r = -1, n
        i, j = 0, -1
        res = []
        # move till the bound
        while len(res) < m*n:
            #print(res)
            while len(res) < m*n and j+1 < r:
                #print(res)
                j += 1
                curr = matrix[i][j]
                res.append(curr)
            t += 1
            
            #print(res)
            while len(res) < m*n and i+1 < b:
                #print(res)
                i += 1
                curr = matrix[i][j]
                res.append(curr)   
            r -= 1
            #print(res)
            while len(res) < m*n and j-1 > l:
                #print(res)
                j -= 1
                curr = matrix[i][j]
                res.append(curr)
                
            b -= 1

            while len(res) < m*n and i-1 > t:
                #print(res)
                i -= 1
                curr = matrix[i][j]
                res.append(curr)

            l += 1


        return res