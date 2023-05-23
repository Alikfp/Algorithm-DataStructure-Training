from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j = 0, 0
        st, end = None, None
        missing = len(t)
        to_collect = Counter(t)

        while j < len(s):
            #print(i, j)
            #print(to_collect)
            #print('Missing', missing)
            if s[j] in to_collect:
                if to_collect[s[j]] > 0:
                    missing -= 1
                to_collect[s[j]] -= 1
            #print(i, j)
            #print(to_collect)
            #print('Missing', missing)
            while i <= j and missing == 0:
                #print('Bringing right pointer forward')
                if (end is None) or (end-st > j-i):
                    end, st = j, i

                if s[i] in to_collect:
                    if to_collect[s[i]] == 0:
                        missing += 1
                    to_collect[s[i]] += 1                    
                i += 1
            
            j += 1
        
        return s[st:end+1] if end is not None else ""