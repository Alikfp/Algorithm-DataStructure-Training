class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cits = sorted(citations)[::-1]
        i = 1
        for cit_count in cits:
            if cit_count < i:
                return i-1
            i += 1
        return i-1 