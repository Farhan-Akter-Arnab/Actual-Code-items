def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp

def print_array(a, a_size):
    for i in range(a_size):
        print("%d" % a[i], end=' ')
    print("\n")

a = [2, 8, 10, 12, 16, 24]
print("Original array: \n")
print_array(a, len(a))

n = 3
rotations(a, n, len(a))

print("Array after ", n, " rotations: \n")
print_array(a, len(a))