def search(root, target):
    if root == None:
        return root
    
    curr = root

    while curr != None:
        if curr.val == target:
            return curr

        if curr.val > target :
            curr = curr.left
        else :
            curr = curr.right
        
    
    return curr

# Important

def deleteNode(root, key):
    if root is None:
            return None
        
    if key < root.val:
            root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            temp = root.right
            while temp.left is not None:
                temp = temp.left
                    
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)

    return root


# Validate Binary Tree

def check(root, mn, mx):
    if root is None:
        return True
    
    if root.val < mn or root.val > mx:
        return False
    
    checkLeft = check(root.left, mn, root.val - 1)
    checkRight = check(root.right, root.val + 1, mx)
    return checkLeft and checkRight

def isValidBST(root):
    return check(root, -10000000000000, 10000000000000)

# Find kth smallest element in a binary tree

def kth_smallest(root, k):
    pass