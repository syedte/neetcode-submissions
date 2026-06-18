# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        bfs = deque([root])
        while bfs:
            for i in range(len(bfs)):
               node= bfs.popleft()
               if node.left:
                bfs.append(node.left)
               if node.right:
                bfs.append(node.right) 
            level +=1
        return level
            

        