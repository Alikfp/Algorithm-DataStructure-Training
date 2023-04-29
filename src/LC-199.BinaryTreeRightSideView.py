# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, l=0):
            if l == len(res):
                res.append(node.val)
            if node.right:
                dfs(node.right, l+1)
            if node.left:
                dfs(node.left, l+1)

        if root is None:
            return []
        dfs(root)
        return res

            
