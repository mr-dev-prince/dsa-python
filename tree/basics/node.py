class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

root = Node(5)
root.left = Node(6)
root.right = Node(8)

