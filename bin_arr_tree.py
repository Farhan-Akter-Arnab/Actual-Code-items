tree = [None] * 10
def ensure_capacity(index):
    if index >= len(tree): new_size = max(index + 1, len(tree) * 2); tree.extend([None] * (new_size - len(tree)))
def root(key):
    if tree[0] is not None: raise Exception("Root already exists")
    else: tree[0] = key
def set_left(key, parent):
    child_index = 2 * parent + 1
    if parent >= len(tree) or tree[parent] is None: raise Exception(f"Can't set left child at index {child_index}, no parent found at index {parent}")
    else: ensure_capacity(child_index); tree[child_index] = key
def set_right(key, parent):
    child_index = 2 * parent + 2
    if parent >= len(tree) or tree[parent] is None: raise Exception(f"Can't set right child at index {child_index}, no parent found at index {parent}")
    else: ensure_capacity(child_index); tree[child_index] = key
def print_tree():
    for i, value in enumerate(tree):
        if value is not None: print(f"{value} at index {i}", end=" ")
        else: print("- ", end=""); print()
def print_tree_visual(index, indent=0):
    if index < len(tree) and tree[index] is not None:
        print_tree_visual(2 * index + 2, indent + 4); print(" " * indent + str(tree[index])); print_tree_visual(2 * index + 1, indent + 4)
root('O')
set_left('A', 0); set_right('B', 0); set_left('C', 1); set_right('D', 1); set_left('E', 2); set_right('F', 2); set_left('G', 3); set_right('H', 3); set_left('I', 4)
print("Array representation of the tree:"); print_tree(); print("\nVisual representation of the tree:"); print_tree_visual(0)