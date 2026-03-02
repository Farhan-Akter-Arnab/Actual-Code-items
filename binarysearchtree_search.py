class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)
key = int(input("Enter the key to search: "))
result = search(root, key)
if result:
    print("Key found:", result.val)
else:
    print("Key not found.")