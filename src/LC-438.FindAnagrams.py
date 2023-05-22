from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sample = Counter(p)
        m = len(p)
        i = 0
        res = []
        while i+m-1 < len(s):
            if Counter(s[i:i+m]) == sample:
                res.append(i)
            i += 1
            if i+m-1 < len(s) and s[i+m-1] not in sample:
                i += m
        return res