from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        timer = 0
        rots = []
        # find all the rots
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rots.append((i,j))
        

        nxt = deque(rots)
        while nxt:
            #print('nxt', nxt)
            level = nxt
            nxt = deque([])

            while level:
                curr = level.popleft()
                #print('curr', curr)
                # Get all the legit neighbors
                adjs = []
                x, y = curr[0], curr[1]
                for x, y in [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
                    if (0 <= x < len(grid)) and (0 <= y < len(grid[0])):
                        adjs.append((x,y))

                # Get rot all neighbors, increment the count by one
                for ad in adjs:
                    if grid[ad[0]][ad[1]] == 1:
                        grid[ad[0]][ad[1]] = 2
                        nxt.append(ad)
                #print('nxt', nxt)
            if nxt :
                timer += 1

        for r in grid:
            for cell in r:
                if cell == 1:
                    return -1
        return timer