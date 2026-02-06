from binarytree import Node
root = Node(1)
root.left, root.right = Node(2), Node(3)
root.left.left, root.left.right = Node(4), Node(5)
root.right.left, root.right.right = Node(6), Node(7)
print("Binary Tree structure: "); print(root)
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)
def pre_order_traversal(node):
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')
print("\nIn-order Traversal: ", end=''); in_order_traversal(root)
print("\nPre-order Traversal: ", end=''); pre_order_traversal(root)
print("\nPost-order Traversal: ", end=''); post_order_traversal(root)