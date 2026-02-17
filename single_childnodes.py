class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
def print_single_child_nodes(root):
    if root is None:
        return []
    result = []
    if (root.left is None and root.right is not None) or (root.right is None and root.left is not None):
        result.append(root.data)
    result += print_single_child_nodes(root.left)
    result += print_single_child_nodes(root.right)
    return result
# Driver code
root = Node(1)
root.left = Node(2); root.right = Node(3)
root.left.right = Node(4); root.left.right.left = Node(5); root.right.right = Node(6)
root.right.right.left = Node(7); root.right.right.right = Node(8); root.right.right.left.right = Node(9)
ans = print_single_child_nodes(root)
if ans:
    print(*ans)
else:
    print(-1)