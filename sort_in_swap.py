def sortArray(A):
    if len(A) <= 1:
        return
    x = -1
    y = -1
    prev = A[0]
    for i in range(1, len(A)):
        if prev > A[i]:
            if x == -1:
                x = i - 1
                y = i
            else:
                y = i
        prev = A[i]
    swap(A, x, y)
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
if __name__ == "__main__":
    a = [3, 5, 6, 9, 8, 7, 10, 4]
    print("Original array:", a)
    sortArray(a)
    print("Sorted array:", a)