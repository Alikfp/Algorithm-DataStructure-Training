class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        while i < len(t) and j < len(s):
            curr_char = t[i]
            while j < len(s):
                if s[j] == curr_char:
                    i += 1
                    j += 1
                    break
                j += 1
            
        return len(t) - i