class Node:
    def __init__(self, data):
        self.left_child = None
        self.data = data
        self.right_child = None
def find_size_recursive(root):
    if root is None: return 0
    return find_size_recursive(root.left_child) + find_size_recursive(root.right_child) + 1
def find_size_iterative(root):
    if root is None: return 0
    count = 0; stack = []; stack.append(root)
    while stack:
        node = stack.pop(); count += 1
        if node.left_child is not None: stack.append(node.left_child)
        if node.right_child is not None: stack.append(node.right_child)
    return count
root = Node(1); root.left_child = Node(2); root.right_child = Node(3)
root.left_child.left_child = Node(4); root.left_child.right_child = Node(5)
root.right_child.left_child = Node(6); root.right_child.right_child = Node(7)
root.right_child.left_child.left_child = Node(8); root.right_child.left_child.right_child = Node(9)
size_recursive = find_size_recursive(root)
print(f"The size of the binary tree (recursive) is {size_recursive}")
size_iterative = find_size_iterative(root)
print(f"The size of the binary tree (recursive) is {size_iterative}")