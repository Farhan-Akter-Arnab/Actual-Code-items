def mergeSorting(A):
    if len(A) > 1:
        mid = len(A) // 2
        left, right = A[:mid], A[mid:]
        mergeSorting(left)
        mergeSorting(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
A = [59, 80, 38, 17, 90, 31, 56, 55, 24, 8, 21, 10]
print("Unsorted Array: {}".format(A))
mergeSorting(A)
print("Sorted Array: {}".format(A))