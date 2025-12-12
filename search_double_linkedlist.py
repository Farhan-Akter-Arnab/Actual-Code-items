class Node:
    def __init__(self, data):
        self.data = data; self.prev = None; self.next = None
class DoublyLL:
    def __init__(self):
        self.head = None
    def searching(self, data):
        t = 0; temp = self.head
        while temp:
            if temp.data == data:
                t = 1; break
            temp = temp.next
        if t == 1: print("Element found!") 
        else: print("Hmm... ... Element not found...")
    def display(self):
        if self.head == None: print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <--> ")
                temp = temp.next
l = DoublyLL()
n = Node(10); l.head = n; n1 = Node(24); n.next = n1; n2 = Node(8); n2.prev = n1; n1.next = n2; n3 = Node(20); n3.prev = n2; n2.next = n3; n4 = Node(12); n4.prev = n3; n3.next = n4; n5 = Node(30); n5.prev = n4; n4.next = n5; n6 = Node(32); n6.prev = n5; n5.next = n6; n7 = Node(40); n7.prev = n6; n6.next = n7
l.display(); print(end="\n"); l.searching(40); l.searching(100)