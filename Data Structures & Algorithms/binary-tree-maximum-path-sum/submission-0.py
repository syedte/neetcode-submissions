# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            lefmax = dfs(root.left)
            rigmax = dfs(root.right)
            lefmax = max(lefmax, 0)
            rigmax = max(rigmax, 0)

            res[0] = max(res[0], root.val + lefmax + rigmax)

            return root.val + max(lefmax, rigmax)
        dfs(root)
        return res[0]
            
        