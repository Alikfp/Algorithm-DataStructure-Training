from collections import Counter
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for word in strs:
            c = Counter(word)
            k = ''.join(sorted(word))
            if k in res:
                res[k] += [word]
            else:
                res[k] = [word]

        return [vals for key, vals in res.items()]
