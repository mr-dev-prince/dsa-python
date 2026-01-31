from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    total = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        mp = defaultdict(int)
        mp[0] = 1

        def findPathSum(cur, curSum):
            if not cur : return

            curSum += cur.val

            if mp[curSum - targetSum]:
                self.total += mp[curSum - targetSum]
                
            mp[curSum] += 1

            findPathSum(cur.left, curSum)
            findPathSum(cur.right, curSum)

            mp[curSum] -= 1
            return
            
        findPathSum(root, 0)
        return self.total