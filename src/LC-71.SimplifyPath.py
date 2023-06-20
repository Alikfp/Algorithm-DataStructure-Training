class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        parsed = path.split("/")
        #print(parsed)
        for c in parsed:
            if stk and c == "..":
                    stk.pop()
            elif c not in ['.', '..', '']:
                stk.append(c)
        return "/" + "/".join(stk)