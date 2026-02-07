class Node:
    def __init__(self, key): self.key = key; self.left = None; self.right = None
class BST:
    def __init__(self): self.root = None
    def insert(self, key): self.root = self._insert(self.root, key)
    def _insert(self, node, key):
        if node is None: return Node(key)
        if key < node.key: node.left = self._insert(node.left, key)
        else: node.right = self._insert(node.right, key)
        return node
    def search(self, key): return self._search(self.root, key)
    def _search(self, node, key):
        if node is None or node.key == key: return node
        if key < node.key: return self._search(node.left, key)
        return self._search(node.right, key)
    def delete(self, key): self.root = self._delete(self.root, key)
    def _delete(self, node, key):
        if node is None: return node
        if key < node.key: node.left = self._delete(node.left, key)
        elif key > node.key: node.right = self._delete(node.right, key)
        else:
            if node.left is None: return node.right
            if node.right is None: return node.left
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node
    def _min_value_node(self, node):
        current = node
        while current.left: current = current.left
        return current
bst = BST()
bst.insert(50); bst.insert(30); bst.insert(20); bst.insert(40); bst.insert(70); bst.insert(60); bst.insert(80)
print(bst.search(40).key if bst.search(40) else "Not found")
bst.delete(20); bst.delete(30); bst.delete(50)
print(bst.search(30).key if bst.search(20) else "Not found")