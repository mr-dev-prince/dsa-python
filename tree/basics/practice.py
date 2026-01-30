from collections import defaultdict, deque
from tree.basics.node import Node

ans = []

def pre_order(root: Node):
    # base case
    if root is None:
        return 
    
    ans.append(root.val)
    pre_order(root.left)
    pre_order(root.right)

def post_order(root: Node):
    if root is None:
        return 
    
    post_order(root.left)
    ans.append(root.val)
    post_order(root.right)

def right_view(root: Node):
    arr = []

    if root is None:
        return ans

    q = deque()
    q.push(root)
    arr.append(root.val)

    while q.size() > 0:
        level = []

        for _ in range(q.size()):
            curr = q.popleft()

            if curr.left != None:
                level.append(curr.left.val)
                q.append(curr.left)

            if curr.right != None:
                level.append(curr.right.val)
                q.append(curr.right)
        
        if len(arr) > 0:
            arr.append(arr[len(level) - 1])
    
    return arr

def left_view(root: Node):
    arr = []

    if root is None:
        return ans

    q = deque()
    q.push(root)
    arr.append(root.val)

    while q.size() > 0:
        level = []

        for _ in range(q.size()):
            curr = q.pop()

            if curr.left != None:
                level.append(curr.left.val)
                q.append(curr.left)

            if curr.right != None:
                level.append(curr.right.val)
                q.append(curr.right)
        
        if len(arr) > 0:
            arr.append(arr[level[0]])
    
    return arr

def vertical_view(root: Node):
    # we need a data structure that holds 3 values -> [ row, col, val ]
    if not root:
        return []
    
    q = deque([(root, 0)]) # (node, root)

    min_col, max_col = 0, 0

    cols = defaultdict(list) # col index -> list of values

    while q:
        node, col = q.popleft()
        min_col, max_col = min(min_col, col), max(max_col, col)
        cols[col].append(node.val)

        if node.left:
            q.append((node.left, col-1))
        
        if node.right:
            q.append((node.right, col+1))
        
    return [ cols[c] for c in range(min_col, max_col + 1)]

class Triplet:
    def __init__(self, r, c, v):
        self.r = r
        self.c = c
        self.v = v
    
    def get_r(self):
        return self.r
    
    def get_c(self):
        return self.c

    def get_v(self):
        return self.v
