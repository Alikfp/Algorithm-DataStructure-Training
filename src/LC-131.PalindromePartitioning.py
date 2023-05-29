class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(st):
            return st == st[::-1]

        def partial_partition(pref, sub):
            if sub == '':
                res.append(pref)
                return
            for i in range(1, len(sub)+1):
                if is_palindrome(sub[:i]):
                    partial_partition (pref + [sub[:i]], sub[i:])

        partial_partition([], s)
        return res