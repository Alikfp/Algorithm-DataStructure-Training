# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        targets = set(nodes)
        self.ans = 0

        def traverse(root):
            if not root:
                return 0
            
            found_count = traverse(root.left) + traverse(root.right)

            if root in targets:
                found_count += 1
            
            if found_count == len(nodes):
                self.ans = self.ans or root
            
            return found_count
        
        traverse(root)
        return self.ans
