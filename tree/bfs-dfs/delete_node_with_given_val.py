def delNode(root, target):
    def post(root):
        if not root: return None

        post(root.left)
        post(root.right)

        if not root.left and not root.right and root.val == target:
            return None
        else: return root

    
    return post(root)