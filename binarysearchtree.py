class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, item):
    if root is None: return Node(item)
    if item < root.key: root.left = insert(root.left, item)
    elif item > root.key: root.right = insert(root.right, item)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    print("Inorder traversal of the binary search tree is:"); inorder(root)