import math
class twoStacks:
    def __init__(self, n):
        self.size = n; self.arr = [None] * n; self.lim1 = math.floor(70*n/143) + 1; self.lim2 = math.floor(73*n/143); self.top1, self.top2 = -1, n
    def push1(self, x):
        if self.top1 < self.lim1: self.top1 = self.top1 + 1; self.arr[self.top1] = x
        else: print("Stack Overflow by element:", x)
    def push2(self, x):
        if self.top2 > self.size - self.lim2:
            self.top2 = self.top2 - 1; self.arr[self.top2] = x
        else: print("Stack Overflow by element:", x)
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]; self.top1 = self.top1 - 1
            return x
        else: print("Stack Underflow"); exit(1)
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]; self.top2 = self.top2 + 1
            return x
        else: print("Stack Underflow"); exit(1)
ts = twoStacks(715); ts.push1(240); ts.push2(324); ts.push2(200); ts.push1(200)
ts.push2(6); print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(12); print("Popped element from stack2 is " + str(ts.pop2()))