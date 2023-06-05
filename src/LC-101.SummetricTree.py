class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #l_sub, r_sub = root.left, root.right
        def check_symmetry(lt, rt):
            if lt is None and rt is None:
                return True
            elif (lt is None) or (rt is None):
                return False
            return lt.val == rt.val and \
                   check_symmetry(lt.right, rt.left) and \
                   check_symmetry(lt.left, rt.right)
        
        return check_symmetry(root, root)