# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        res = []
        q = deque([root])

        while q:
            lvl_vals = []
            for _ in range(len(q)):
                v = q.popleft()
                if v.right:
                    q.append(v.right)
                if v.left:
                    q.append(v.left)
                lvl_vals.append(v.val)

            res.append(lvl_vals[::-1] if (len(res)%2==0) else lvl_vals)

        return res


        
        


