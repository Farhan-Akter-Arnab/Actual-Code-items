class Node:
    def __init__(self, data): self.data = data; self.left = None; self.right = None
def has_path_sum(node, target_sum):
    if node is None: return False
    remaining_sum = target_sum - node.data
    if remaining_sum == 0 and node.left is None and node.right is None: return True
    return has_path_sum(node.left, remaining_sum) or has_path_sum(node.right, remaining_sum)
def find_paths_in_range(node, low, high, current_path=None, current_sum=0, valid_paths=None):
    if valid_paths is None: valid_paths = []
    if current_path is None: current_path = []
    if node is None: return valid_paths
    current_path.append(node.data); current_sum += node.data
    if node.left is None and node.right is None:
        if low <= current_sum <= high: valid_paths.append(list(current_path))
    else:
        find_paths_in_range(node.left, low, high, current_path, current_sum, valid_paths); find_paths_in_range(node.right, low, high, current_path, current_sum, valid_paths)
    current_path.pop(); return valid_paths
if __name__ == "__main__":
    target_sum = 24; root = Node(8); root.left = Node(8); root.right = Node(2); root.left.left = Node(3); root.left.left.right = Node(5); root.left.right = Node(5); root.right.right = Node(7)
    if has_path_sum(root, target_sum): print(f"There is a root-to-leaf path with sum {target_sum}.")
    else: print(f"There is no root-to-leaf path with sum {target_sum}.")
    low, high = 8, 24; paths = find_paths_in_range(root, low, high)
    print(f"Root-to-leaf paths with sums in the range [{low}, {high}]:")
    for path in paths: print(" -> ".join(map(str, path)))