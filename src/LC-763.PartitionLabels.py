class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = {char:i for i, char in enumerate(s)}
        res = []
        counter = 1
        mx_end = ends[s[0]]
        for j in range(len(s)):
            mx_end = max(mx_end, ends[s[j]])
            if mx_end == j:
                res.append(counter)
                counter = 0
            counter += 1
        return res