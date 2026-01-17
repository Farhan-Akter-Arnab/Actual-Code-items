class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def isempty(self):
        return self.head is None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.isempty():
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped
    def peek(self):
        if self.isempty():
            return None
        return self.head.data
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  # Output: 30 -> 20 -> 10 -> None
print(stack.pop())  # Output: 30
print(stack.peek()) # Output: 20
stack.display()  # Output: 20 -> 10 -> None