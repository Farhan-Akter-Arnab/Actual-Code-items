class Node:
    # A class representing a node in a binary tree
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    @staticmethod
    def max_depth(node):
        # Recursively calculates the maximum depth (height) of the binary tree
        if node is None:
            return 0
        left_depth = Node.max_depth(node.left)
        right_depth = Node.max_depth(node.right)
        return max(left_depth, right_depth) + 1
if __name__ == '__main__':
    # Constructing the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    # Calculating and printing the height of the tree
    height = Node.max_depth(root)
    print(f"Height of the tree is {height}")