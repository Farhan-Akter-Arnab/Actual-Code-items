class newNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None
def traverse(root, tilt):
    if not root:
        return 0
    left = traverse(root.left, tilt)
    right = traverse(root.right, tilt)
    tilt[0] += abs(left - right)
    return left + right + root.val
def Tilt(root):
    tilt = [0]
    traverse(root, tilt)
    return tilt[0]
if __name__ == "__main__":
    root = None
    root = newNode(89)
    root.left = newNode(80)
    root.right = newNode(97)
    root.left.left = newNode(64)
    root.left.right = newNode(88)
    root.right.right = newNode(72)
    print("The tilt of the whole tree is", Tilt(root))