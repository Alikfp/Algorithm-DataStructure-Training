from collections import Counter
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = Counter(s)
        sorted_counter = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        total = 0
        for i, (k, v) in enumerate( sorted_counter.items()):
            total += (i//9 + 1)*v
        return total
