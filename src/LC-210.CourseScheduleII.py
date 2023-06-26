class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        visited = {i:0 for i in range(numCourses)}
        path = []
        self.cycle = False
        for d, s in prerequisites:
            g[d].add(s)

        def dfs(st):
            if self.cycle: return 
            if visited[st] == 1:
                self.cycle = True
                return
            if visited[st] == 0:
                visited[st] = 1
                for nei in g[st]:
                    dfs(nei)
                visited[st] = 2
                path.append(st)

        for i in range(numCourses):
            if self.cycle: return []
            if visited[i] == 0:
                dfs(i)
        
        return path