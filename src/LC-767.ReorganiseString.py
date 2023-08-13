from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        hp = [(-value,key) for key,value in c.items()] + [(float('inf'),"")]
        heapq.heapify(hp)
        res = ""
        while len(hp) > 1:
            c1, l1 = heapq.heappop(hp)
            c2, l2 = heapq.heappop(hp)
            res += l1
            res += l2
            if c1+1 < 0:
                heapq.heappush(hp, (c1+1, l1))
            if c2+1 < 0:
                heapq.heappush(hp, (c2+1, l2))
        
        return res if len(res)==len(s) else ""