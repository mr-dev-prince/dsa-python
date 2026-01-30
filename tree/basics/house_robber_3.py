class Solution:
    def rob(self, root):
        def dfs(root):
            if not root:
                return [0, 0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            # if you rob root, you can't rob its children
            withR = root.val + leftPair[1] + rightPair[1]
            # if you skip root, you can rob any of the children
            withoutR = max(leftPair) + max(rightPair)

            return [withR, withoutR]
        
        return max(dfs(root))