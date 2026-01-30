def find_height(root):
    # base
    if not root:
        return 0
    
    # hypothesis
    lh = find_height(root.left)
    rh = find_height(root.right)

    # induction
    return 1 + max(lh, rh)

