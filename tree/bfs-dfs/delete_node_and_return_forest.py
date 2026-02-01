from typing import Optional, List
from construct_string_from_binary_tree import TreeNode

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        todelete = set(to_delete)
        ans = []

        def pre(root):
            if not root: return 

            if root.val in todelete:
                if root.left and root.left.val not in todelete:
                    ans.append(root.left)
                if root.right and root.right.val not in todelete:
                    ans.append(root.right)

            pre(root.left)
            if root.left and root.left.val in todelete:
                root.left = None

            pre(root.right)
            if root.right and root.right.val in todelete:
                root.right = None
            
        pre(root)
        if root.val not in todelete:
            ans.append(root)
        return ans