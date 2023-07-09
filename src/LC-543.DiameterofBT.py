class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def get_depth(root):
            if root is None: return 0
            l, r = get_depth(root.left), get_depth(root.right)
            self.res = max(self.res, l+r)
            return 1 + max(l, r)
        
        get_depth(root)
        return self.res