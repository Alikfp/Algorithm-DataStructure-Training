class Solution:
    def partitionString(self, s: str) -> int:
        counter = 0
        curr_part = set()
        for c in s:
            #print(curr_part)
            if c not in curr_part:
                curr_part.add(c)
            else:
                counter += 1
                curr_part = set([c])
        return counter + 1