class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_ll(head: Node):
    curr = head
    while curr != None:
        print(curr.data, end=" -> ")
        curr = curr.next

def insert_at_end(head: Node, newNode : Node):
    curr = head
    
    while curr.next != None:
        curr = curr.next
    
    curr.next = newNode
    return head

def insert_at_start(head: Node, newNode: Node):
    newNode.next = head
    return newNode

def insert_at_kth(head: Node, newNode: Node, pos : int):
    curr = head

    for i in range(pos - 1):
        curr = curr.next
    
    newNode.next = curr.next
    curr.next = newNode
    return head

def delete_from_start(head : Node):
    return head.next

def delete_from_end(head : Node):
    curr = head

    while curr.next.next != None:
        curr = curr.next

    curr.next = None
    return head

def delete_kth(head : Node, pos : int):
    if pos == 1:
        return head.next
    
    curr = head

    for _ in range(pos - 2):
        if curr is None or curr.next is None:
            return head
        curr = curr.next
    
    if curr.next:
        curr.next = curr.next.next
    return head

# Creating Objects
a = Node(10)
b = Node(5)
c = Node(3)

a.next = b
b.next = c

head = a

# print_ll(head)
head = insert_at_start(head, Node(7))
head = insert_at_end(head, Node(15))
head = insert_at_kth(head, Node(18), 3)
head = delete_from_start(head)
head = delete_from_end(head)
head = delete_kth(head, 2)
print_ll(head)
