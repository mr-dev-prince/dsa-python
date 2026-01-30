# LC 235 - Lowest Common Ancestor in BST

# -> given root, p, q where p and q are nodes of the tree, we have to find a node that is common ancestor of p and q

# -> A node can be decendent of itself, which means a node can be ancestor of itself

# -> Solution
# if p and q are greater than curr node -> we gonna find them on right
# if p and q are lesser than curr node -> we gonna find them on left
# if it is less than one and greater than the other -> curr node is the answer

def lcaInBSTree(root, p, q):
    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr
    

# LC 236 - LCA in Binary Tree

# solution

# -> Brute -> find all the ancestor of the two given nodes - return the lowest common ancestor

# -> Optimal -> use recursion to find the common ancestor on left and right
    # -> base case - if root is null || if root == p || if root == q --> return root - because one of the nodes is root itself which can be ancestor of it self
    # -> induction - if you found p and q on left-right or right-left - it means the node you are currently at is the ancestor of both given nodes -> return it
    # -> if you found the p or q on left and right is null -> it means that both given nodes exist on the left subtree -> return left 
    # -> if you found the p or q on right and left is null -> it means that both given nodes exist on the right subtree -> return right

def lcaInBTree(root, p, q):
    if not root or root == p or root == q:
        return root
    
    leftLca = lcaInBTree(root.left, p, q)
    rightLca = lcaInBTree(root.right, p, q)

    if leftLca and rightLca:
        return root
    
    return leftLca if leftLca else rightLca
