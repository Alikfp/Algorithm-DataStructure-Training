# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # construct a sorted list 
        delta = float("inf")
        last = float("inf")

        def in_order (root):
            nonlocal delta, last
            if root is None: return
            if root.left:
                in_order(root.left)
            delta = min(delta, root.val-last) if last != float("inf") else float("inf")
            last = root.val
            if root.right:
                in_order(root.right)

        in_order(root)
        return delta
        