class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        a, b = dict(), dict()
        for x, y in zip(s, t):
            if (x in a) and (a[x] != y) or (y in b) and (b[y] != x): return False
            a[x] = y
            b[y] = x
        return True