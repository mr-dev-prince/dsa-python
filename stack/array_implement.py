class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
    
    def push(self, x):
        if self.top == self.size - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = x
    
    def pop(self):
        if self.top == -1:
            raise Exception("Stack Underflow")
        val = self.stack[self.top]
        self.top -= 1
        return val
    
    def peek(self):
        if self.top == -1:
            raise Exception("Stack is empty")
        return self.stack[self.top]
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.size

s = Stack(5)

s.push(5)
s.push(4)
s.pop()

print(s.peek())