from typing import Optional
from construct_string_from_binary_tree import TreeNode

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    maxDiff = float("-inf")

    def helper(root, curMax, curMin):
        nonlocal maxDiff
        if not root: return 

        diff = abs(curMax - curMin)
        maxDiff = max(maxDiff, diff)

        if root.left:
            helper(root.left, max(curMax, root.left.val), min(curMin, root.left.val))
        if root.right:
            helper(root.right, max(curMax, root.right.val), min(curMin, root.right.val))

    helper(root, root.val, root.val, 0)
    return maxDiff