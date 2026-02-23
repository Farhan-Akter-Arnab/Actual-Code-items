class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def print_k_levels_down(node, k):
    if node is None or k < 0:
        return
    if k == 0:
        print(node.data)
        return
    print_k_levels_down(node.left, k - 1)
    print_k_levels_down(node.right, k - 1)
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)
    k = 2
    print(f"Nodes at distance {k} from the root:")
    print_k_levels_down(root, k)