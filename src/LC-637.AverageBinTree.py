# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        avs = []
        while q:
            lvl_sum = 0
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                lvl_sum += curr.val
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
            avs.append(lvl_sum/n)
        return avs