def reorder(root):
    prev = None # to check if the current val is not inorder 
    first = None # for first violation
    second = None # for second violation

    def inorder(node):
        if not node:
            return
        
        inorder(node.left)

        if prev and prev.val > node.val: # means that the current val is less than prev val - violation
            if not first:
                first = node 
            second = node # we are guaranteed that there will be two swapped values
        
        prev = node

        inorder(node.right)
    
    inorder(root)

    first.val, second.val = second.val, first.val