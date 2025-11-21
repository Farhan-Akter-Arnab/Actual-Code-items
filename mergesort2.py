def mergeSorting(A):
    if len(A) > 1:
        mid = len(A) // 2
        left, right = A[:mid], A[mid:]
        mergeSorting(left)
        mergeSorting(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            A[k] = left[i] if left[i] < right[j] else right[j]
            i, j = (i + 1, j) if left[i] < right[j] else (i, j + 1)
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

A = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Unsorted Array: {}".format(A))
mergeSorting(A)
print("Sorted Array: {}".format(A))