class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_height(root):
            if not root:
                return 1
            return 1 + get_height(root.left)

        Solution.total = 0
        def helper(root):

            if root is None:
                return
            h = get_height(root.left)
            if get_height(root.right) == h:
                Solution.total += (2**(h-1))
                helper(root.right)
            elif get_height(root.right) < h:
                Solution.total += (2**(h-2))
                helper(root.left)
        helper(root)
        return Solution.total