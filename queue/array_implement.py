class Queue:
    def __init__(self):
        self.q = []
        self.front = 0

    def push(self, val):
        self.q.append(val)

    def pop(self):
        if self.front >= len(self.q):
            return -1
        x = self.q[self.front]
        self.front += 1
        return x

    def get_front(self):
        if self.front >= len(self.q):
            return -1
        return self.q[self.front]

    def size(self):
        return len(self.q) - self.front