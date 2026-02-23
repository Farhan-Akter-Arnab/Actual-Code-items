class Node:
    def __init__(self, data):
        self.data = data; self.left = None; self.right = None
class Info:
    def __init__(self, is_bst, size, min_val, max_val):
        self.is_bst = is_bst
        self.size = size
        self.min = min_val
        self.max = max_val
def largest_bst(root):
    def helper(node):
        if node is None: return Info(True, 0, float('inf'), float('-inf'))
        left, right = helper(node.left), helper(node.right)
        if left.is_bst and right.is_bst and left.max < node.data < right.min:
            size = left.size + right.size + 1
            min_val = min(node.data, left.min)
            max_val = max(node.data, right.max)
            return Info(True, size, min_val, max_val)
        else: return Info(False, max(left.size, right.size), 0, 0)
    return helper(root).size
if __name__ == "__main__":
    root = Node(50); root.left = Node(30); root.right = Node(60); root.left.left = Node(5)
    root.left.right = Node(20); root.right.left = Node(45); root.right.right = Node(70); root.right.right.right = Node(80)
    print("Size of the largest BST is:", largest_bst(root))