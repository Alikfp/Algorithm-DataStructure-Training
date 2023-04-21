class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palin_scan(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        res = ''
        for i in range(len(s)):
            res = max(palin_scan(i, i), palin_scan(i, i+1), res, key=len)
        return res
    
    