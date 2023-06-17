class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words =  s.split(' ')
        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):
            return False
        l_to_w = dict()
        for l, w in zip(pattern,words):
            if (l in l_to_w):
                if (l_to_w[l] != w):
                    return False
            else:
                l_to_w[l] = w
        return True
