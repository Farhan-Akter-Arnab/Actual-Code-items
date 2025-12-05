class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SingleLL:
    def __init__(self):
        self.head = None
    def swap(self, n1, n2):
        prevNode1 = None
        prevNode2 = None
        node1 = self.head
        node2 = self.head
        if (self.head == None): return
        if (n1 == n2): return
        while (node1 != None and node1.data != n1):
            prevNode1 = node1
            node1 = node1.next
        while (node2 != None and node2.data != n2):
            prevNode2 = node2
            node2 = node2.next
        if (node1 != None and node2 != None):
            if (prevNode1 != None):
                prevNode1.next = node2
            else:
                self.head = node2
            if (prevNode2 != None):
                prevNode2.next = node1
            else:
                self.head = node1
            temp = node1.next
            node1.next = node2.next
            node2.next = temp
        else:
            print("Swapping is not possible")
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node       
        self.head = prev              
    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
# Driver code
l = SingleLL()
n= Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
l.display()
print(end='\n')
l.reverse()
l.display()