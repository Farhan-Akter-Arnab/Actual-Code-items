class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def getPreIndex(): return constructTreeIII.preIndex
def IncrementPreIndex(): constructTreeIII.preIndex += 1
def constructTreeIII(pre, low, high):
    if low > high: return None
    root = Node(pre[getPreIndex()]); IncrementPreIndex()
    if low == high: return root
    split = low
    while split <= high and pre[split] <= root.data: split += 1
    root.left = constructTreeIII(pre, getPreIndex(), split - 1)
    root.right = constructTreeIII(pre, split, high); return root
def constructTree(pre):
    size = len(pre); constructTreeIII.preIndex = 0
    return constructTreeIII(pre, 0, size - 1)
def printInorder(root):
    if root is None: return
    printInorder(root.left); print(root.data, end=' '); printInorder(root.right)
pre = [10, 5, 3, 7, 40, 50, 8, 24]; root = constructTree(pre)
print("Inorder traversal of the constructed tree is: ", end='')
printInorder(root)