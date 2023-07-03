# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, d=1):
        if root is None: return
        self.mx_depth = max(self.mx_depth, d)
        self.dfs(root.right, d+1)
        self.dfs(root.left, d+1)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.mx_depth = 0
        self.dfs(root)
        return self.mx_depth