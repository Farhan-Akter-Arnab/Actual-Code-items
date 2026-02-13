class Node:
    # A class representing a node in a binary tree.
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def sum_tree_recursive(root):
    # Recursively calculates the sum of all nodes in the binary tree.
    if root is None:
        return 0
    return sum_tree_recursive(root.left) + sum_tree_recursive(root.right) + root.key
if __name__ == '__main__':
    # Constructing the binary tree
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)
    root.right.left.right = Node(80)
    # Calculating and printing the sum of all nodes
    total_sum = sum_tree_recursive(root)
    print(f"Sum of all the nodes is: {total_sum}")