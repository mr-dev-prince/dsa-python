class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

arr1 = [ 5, 7, 2, 9 ]
arr2 = [ 9, 4 ]

def print_ll(head: Node):
    curr = head

    while curr != None:
        print(curr.data, end=" -> ")
        curr = curr.next

def insert_at_end(head: Node, data: int):
    newNode = Node(data)

    if head == None:
        head = newNode
        return head
    
    curr = head
    while curr.next != None:
        curr = curr.next
    
    curr.next = newNode
    return head

head1 = None
head2 = None

for n in arr1:
    head1 = insert_at_end(head1, n)

for n in arr2:
    head2 = insert_at_end(head2, n)

# LC-876 | Fast & Slow Pointer
def find_middle(head : Node):
    fast = head
    slow = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow

# LC-237 | Delete kth node where head and k isn't given
def delete_node(node : Node):
    # copy the val of next node in the given node 
    # delete the next node
    node.data = node.next.data
    node.next = node.next.next

# LC-19 | Remove kth node from end
def remove_nth_node(head : Node, k : int):
    early = head
    late = head

    for _ in range(k):
        early = early.next

    # edge case - when k == length of LL | meaning you have to remove the first element
    if early == None:
        head = head.next
        return head
    
    while early.next != None:
        early = early.next
        late = late.next
    
    late.next = late.next.next
    return head

# LC-83 | Remove duplicates from a sorted LL
def remove_duplicates(head : Node):
    curr = head

    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head

# LC-206 | Reverse LL
def reverse_ll(head : Node):
    curr = head
    prev = None
    next = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

# LC-234 | Palindrome Linked list
def palindrome_ll(head : Node):
    # reverse the linkedlist
    # have two pointers over the real and the reversed LL
    # if at any point the val differs -> not palindrome
    # if you reach at the end of it -> palindrome
    org = head
    rev = reverse_ll(head)

    while org != None:
        if org.data != rev.data:
            return False
        else:
            org = org.next
            rev = rev.next
    
    return True 

# LC-61 | Rotate List
def rotate_to_right_by_k_pos(head : Node, k : int):
    last = head
    length = 0

    while last.next != None:
        last = last.next
        length += 1
    length += 1

    moves = length - (k % length)

    if moves == length:
        return head


    curr = head
    for _ in range(moves):
        curr = curr.next
    
    last.next = head
    head = curr.next
    curr.next = None

    return head

# LC-160 | Intersection of Two LinkedList
def detect_intersection(head1: Node, head2: Node):
    p1 = head1
    p2 = head2

    l1 = 0
    l2 = 0

    while p1 != None:
        l1 += 1
    
    while p2 != None:
        l2 += 1

    diff = abs(l1 - l2)

    if l1 < l2:
        for _ in range(diff):
            p1 = p1.next
    else:
        for _ in range(diff):
            p2 = p2.next
        
    while p1 != None or p2 != None:
        if p1 == p2:
            return p1.data
    
    return None

# LC-2 | Add Two Numbers
def add_two_nums(head1: Node, head2: Node):
    p1 = head1
    p2 = head2

    carry = 0

    ans = Node(-1)
    temp = ans

    while p1 != None and p2 != None:
        s = p1.data + p2.data + carry
        carry = 0

        if s > 10:
            carry = 1
        
        newNode = Node(s % 10)
        temp.next = newNode
        temp = temp.next
        p1 = p1.next
        p2 = p2.next
    
    while p1 != None:
        s = p1.data + carry
        carry = 0

        if s > 9:
            carry = 1

        newNode = Node(s % 10)
        temp.next = newNode
        temp = temp.next
        p1 = p1.next

    while p2 != None:
        s = p2.data + carry
        carry = 0

        if s > 9:
            carry = 1
        
        newNode = Node(s % 10)
        temp.next = newNode
        temp = temp.next
        p2 = p2.next
    
    return ans.next

# LC-141 | Linkedlist Cycle
def detect_cycle(head: Node):
    if head == None or head.next == None:
        return False
    
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# LC-142 | Start of a Loop in LL
def find_start(head: Node):
    slow = head
    fast = head

    hasCycle = False

    while fast != None and fast.next != None:
        if slow == fast:
            hasCycle = True
        slow = slow.next
        fast = fast.next
    
    if not hasCycle:
        return None
    
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

res = add_two_nums(head1, head2)
print_ll(res)
