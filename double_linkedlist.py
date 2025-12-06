class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLL:
    def __init__(self):
        self.head = None
    def insert_beg(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    def insert_end(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        ne.prev = temp
    def delete_beg(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp = None
    def delete_end(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None
    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
l = DoublyLL()
n = Node(int(input("Enter data for head node: ")))
l.head = n
n1 = Node(int(input("Enter data for second node: ")))
n.next = n1
n2 = Node(int(input("Enter data for third node: ")))
n1.prev = n
n1.next = n2
l.display()
print(end="\n")
l.insert_beg(int(input("Enter data to insert at beginning: ")))
l.display()
print(end='\n')
l.insert_end(int(input("Enter data to insert at end: ")))
l.display()
print(end='\n')
l.delete_beg()
l.display()
print(end='\n')
l.delete_end()
l.display()