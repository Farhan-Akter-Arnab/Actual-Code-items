from collections import deque
class Stack:
    def __init__(self):
        self.q1 = deque(); self.q2 = deque()
    def push(self, x):
        self.q1.append(x)
    def pop(self):
        if not self.q1: return
        while (len(self.q1) != 1):
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def top(self):
        if not self.q1: return
        while (len(self.q1) != 1):
            self.q2.append(self.q1.popleft())
        top = self.q1[0]; self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1; return top
    def size(self):
        return len(self.q1)
if __name__ == '__main__':
    s = Stack()
    s.push(1); s.push(2); s.push(3); s.push(4); print("Current size:", s.size())
    print(s.top()); s.pop(); print(s.top()); s.pop(); print(s.top())
    print("Current size: ", s.size())