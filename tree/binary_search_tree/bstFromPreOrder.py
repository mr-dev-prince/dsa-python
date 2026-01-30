# LC 48 - Construct a BST from preorder of it -> the resultant tree should give the same preorder

# -> BST root node has all the elements lesser on the left and greater on the right
# -> BRUTE -> we can sort the preorder to get inorder and use both of them to build the BST
# -> Better -> Use recursion to build the tree with upper bound on both sides

# -> first element of the preorder will be the root
# -> take the upper bound as infinity
# -> take an i pointer pointing initially to the first element of the preorder
# -> if you have reached the end of the preorder or the element is greater than the upperbound -> return null
# -> create root with the first element in every recursive call -> root = TreeNode(preorder[i])
# -> then call the build function recursively -> root.left = build(root.val) - because on the left we need lesser val than root
#                                             -> root.right = build(bound) - because on the right values can be bigger
# once done return the root


def constructBSTree(self, preorder):
    self.i = 0

    def build(bound = float("inf")):
        if self.i == len(preorder) or preorder[self.i] > bound:
            return None

        # create root
        root = preorder[self.i]
        
        # move i ahead
        self.i += 1

        # build left and right part 
        root.left = build(root.val)
        root.right = build(bound)

        return root
    
    return build()