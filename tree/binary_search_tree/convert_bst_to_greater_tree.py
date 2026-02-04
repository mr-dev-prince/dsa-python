from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.runningSum = 0

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)

            self.runningSum += node.val
            node.val = self.runningSum

            dfs(node.left)

        dfs(root)
        return root