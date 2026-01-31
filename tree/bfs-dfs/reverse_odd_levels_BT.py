from typing import Optional
from collections import deque
from construct_string_from_binary_tree import TreeNode

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
     
        q = deque([root])

        i = 0

        while q:
            if i & 1:
                l, r = 0, len(q) - 1
                # swap the values inside the node only
                while l < r:
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i += 1

        return root
