def partition (A, low, high):
    pivot = A[high]
    i = low - 1
    
    for j in range(low, high):
        if A[j] <= pivot:
            i = i + 1
            (A[i], A[j]) = (A[j], A[i])
    (A[i + 1], A[high]) = (A[high], A[i + 1])
    return (i + 1)

def quickSort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quickSort(A, low, pi - 1)
        quickSort(A, pi + 1, high)

A = [10, 7, 8, 9, 1, 5, 17, 22, 12, 24, 16, 0]
print("A before sorting:")
print(A)
n = len(A) - 1
quickSort(A, 0, n)
print("A after sorting:")
print(A)