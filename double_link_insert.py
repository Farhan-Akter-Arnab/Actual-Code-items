class Node:
    def __init__(self, data):
        self.data = data; self.prev = None; self.next = None
class DoublyLL:
    def __init__(self):
        self.head = None
    def insert_after(self, prev_data, data):
        temp = self.head
        while temp:
            if temp.data == prev_data:  # Find the node with the given data
                new_node = Node(data); new_node.next = temp.next; new_node.prev = temp
                if temp.next: temp.next.prev = new_node
                temp.next = new_node; return
            temp = temp.next
        print(f"Node with data {prev_data} not found.")
    def display(self):
        if self.head == None: print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
l = DoublyLL(); n = Node(8); l.head = n; n1 = Node(24); n.next = n1; n2 = Node(10); n1.prev = n; n1.next = n2; l.display(); print(end="\n")
l.insert_after(int(input("Enter the name of node after which you want to enter new data: ")), int(input("Enter the data to be added: "))); l.display()