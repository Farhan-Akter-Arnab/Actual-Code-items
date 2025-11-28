def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

# Rotate array to the left by 1 place
def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp
    
def printArray(a, a_size):
    for i in range(a_size):
        print("% d" % a[i], end=" ")
    print("\n")
    
# Driver function to test the above functions
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Original array:")
    printArray(a, len(a))
    rotations(a, 3, len(a))
    print("Array after left rotation by", 3, "positions:")
    printArray(a, len(a))