# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def aux_isValidBST(curr, mn=-float('inf'), mx=float('inf')):
            #print(curr)
            #print('mx', mx)
            #print('mn', mn)

            if curr is None:
                return True

            # right case
            if curr.right is not None:
                if not ((curr.val < curr.right.val) and (curr.right.val < mx)):
                    #print(curr.val)
                    #print(curr.right.val)
                    #print('mx', mx)
                    return False

            # left case
            if curr.left is not None:
                
                if not ((curr.val > curr.left.val) and (curr.left.val > mn)):
                    #print(curr.val)
                    #print(curr.left.val)
                    #print('mn', mn)
                    return False
            
            #mn = curr.val if mn == -float('inf') else min(curr.val, mn)
            #mx = curr.val if mx == float('inf') else min(curr.val, mx)
            return aux_isValidBST(
                curr.right,
                mn=curr.val,
                mx=mx) and \
            aux_isValidBST(
                curr.left,
                mn=mn,
                mx=curr.val)    
        
        return aux_isValidBST(root)