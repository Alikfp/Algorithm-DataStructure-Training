class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank: return -1
        def gene_gap(st1, st2):
            return sum(x!=y for x,y in zip(st1, st2))
        q = deque([startGene])
        counter = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)
                if node == endGene:
                    return counter
                q += [g for g in bank if ((gene_gap(node, g)==1) and g not in visited)]

            counter += 1
        return -1


