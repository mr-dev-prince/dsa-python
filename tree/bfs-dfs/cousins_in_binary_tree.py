from collections import deque

def isCousins(root, x, y):
    q = deque([root])

    while q:
        xp = yp = None
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                if node.left.val == x:
                    xp = node
                if node.left.val == y:
                    yp = node
                q.append(node.left)
            if node.right:
                if node.right.val == x:
                    xp = node
                if node.right.val == y:
                    yp = node
                q.append(node.right)
        # After one level
        if xp or yp:
            return xp is not None and yp is not None and xp != yp
    return False

def isCousinsDFS(root, x, y):
    xd = yd = -1
    xp = yp = None

    def helper(node, parent, height):
        nonlocal xd, yd, xp, yp
        if not node:
            return

        if node.val == x:
            xd = height
            xp = parent
        
        if node.val == y:
            yd = height
            yp = parent
        
        helper(root.left, node, height + 1)
        helper(root.left, node, height + 1)
    
    helper(root, None, 0)

    return (xd == yd and xp != yp)
