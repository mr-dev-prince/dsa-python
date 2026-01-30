# doubly ll
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def insert_after(self, new_node):
        new_node.prev = self
        new_node.next = self.next
        if self.next:
            self.next.prev = new_node
        self.next = new_node

a = Node(6)
b = Node(7)
c = Node(8)

a.next = b
b.prev = a
b.next = c
c.prev = b



    