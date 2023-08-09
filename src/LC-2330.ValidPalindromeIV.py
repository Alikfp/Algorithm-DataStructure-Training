class Solution:
    def makePalindrome(self, s: str) -> bool:
        counter = 0
        l, r = 0, len(s)-1
        while r > l and counter < 3:
            if s[l] != s[r]: counter += 1
            r -= 1
            l += 1
        return counter < 3