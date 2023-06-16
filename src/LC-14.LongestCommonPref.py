class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for i in range(len(strs[0])):
            #print("pref")
            curr_char = strs[0][i]
            for w in strs:
                if (i >= len(w) )or (w[i] != curr_char):
                    return pref
            pref += curr_char
        return pref

