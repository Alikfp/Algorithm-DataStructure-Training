class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # step
        while p or q:
            if p:
                if type(p.val) is str: return p
                p.val = str(p.val)
                p = p.parent
            if q:
                if type(q.val) is str: return q
                q.val = str(q.val)
                q = q.parent