# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
                return None
        # make the root
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        subtree_split = inorder.index(root_val)

        # get left sub tree
        left_sub_in = inorder[:subtree_split]
        right_sub_in = inorder[subtree_split+1:]

        # build the subtrees
        root.left = self.buildTree(preorder, left_sub_in)
        root.right = self.buildTree(preorder, right_sub_in)

        return root