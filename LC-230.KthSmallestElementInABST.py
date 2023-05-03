class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.rem = k
        self.aux(root)
        return self.res
        
    def aux(self, node):
        if node is None:
            return
        self.aux(node.left)
        self.rem -= 1
        if self.rem == 0:
            self.res = node.val
        self.aux(node.right)