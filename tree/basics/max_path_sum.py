# LC 124 - Maximum Path Sum

# - Sequence of nodes 
# - Single node is also a path

# ---> Solution

# for every node - find what is max path on left and right
# because it is a sequence - if a node has only two children and those are leaf nodes -> then sum is going to be -> leftVal + rootVal + rightVal
# for each node we also need return value -> rootVal + max(leftVal, rightVal)

def maxPathSum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        leftMax = max(leftMax, 0) # if leftMax is -ve, we don't include it
        rightMax = max(rightMax, 0) # if rightMax is -ve, we don't include it

        # compute max path sum WITH split and update max - for node having only two children and those are leaf nodes
        root[0] = max(res[0], root.val + leftMax + rightMax)

        # return value without split - for node having further childrens
        return root.val + max(leftMax, rightMax)
    
    dfs(root)
    return res[0]
