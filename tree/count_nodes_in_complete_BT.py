class Solution:
    def getNoOfNodes(self, root, l):
        temp = root
        h = 0

        while temp:
            h += 1
            temp = temp.left if l else temp.right
        return h

    def countNodes(self, root):
        if not root:
            return 0

        ln = self.getNoOfNodes(root.left, True)
        rn = self.getNoOfNodes(root.right, False)

        if ln == rn : # case of perfect binary tree
            return (2 ** (ln + 1)) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# intuition :
    # - if the subtree is perfect BT - no. of nodes would be -> (2 ** (ln + 1) - 1)
    # - other-wise find the no. of nodes on left and right and [ return 1 (for the curr node) + nodes on left + nodes on right ]