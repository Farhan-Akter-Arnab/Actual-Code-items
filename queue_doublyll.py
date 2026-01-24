class Oghuz_Khan:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None
    def __init__(self):
        self.front = None
        self.rear = None
        self.Size = 0
    def isEmpty(self):
        return self.front is None
    def size(self):
        return self.Size
    def insertFront(self, data):
        newNode = Oghuz_Khan.Node(data)
        if self.front is None:
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode
        self.Size += 1
    def insertRear(self, data):
        newNode = Oghuz_Khan.Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode
        self.Size += 1
    def deleteFront(self):
        if self.isEmpty():
            print("Deque is Empty")
            return
        temp = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.Size -= 1
        del temp
    def deleteRear(self):
        if self.isEmpty():
            print("Deque is Empty")
            return
        temp = self.rear
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.Size -= 1
        del temp
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.front.data
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.rear.data
    def display(self):
        if self.isEmpty():
            print("Deque is Empty")
            return
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
if __name__ == '__main__':
    dq = Oghuz_Khan()
    dq.insertFront(10)
    dq.insertFront(20)
    dq.insertRear(30)
    dq.insertRear(40)
    print("Deque elements: ")
    dq.display()
    print("Size of Deque:", dq.size())
    print("Front element:", dq.getFront())
    print("Rear element:", dq.getRear())
    dq.deleteFront()
    dq.deleteRear()
    print("Deque elements after deletions: ")
    dq.display()