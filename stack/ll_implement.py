class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = Node(-1)
    
    def push(self, x):
        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode
    
    def pop(self):
        if self.top is None:
            raise Exception("Stack Underflow")
        val = self.top.data
        self.top = self.top.next
        return val
    
    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.data
