def sortArray(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        sortArray(L)
        sortArray(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]: arr[k], i = L[i], i + 1
            else: arr[k], j = R[j], j + 1
            k += 1
        while i < len(L): arr[k] = L[i]; i += 1; k += 1
        while j < len(R): arr[k] = R[j]; j += 1; k += 1
def intersectionOfArrays(A1, A2, m, n):
    i = j = 0; A = []
    while i < m and j < n:
        if A1[i] == A2[j]: A.append(A1[i]); i += 1; j += 1
        elif A1[i] < A2[j]: i += 1
        else: j += 1
    print("Intersection of two arrays is: ", A)
A1, A2 = [1, 8, 6, 24, 27, 54], [10, 26, 8, 6, 10, 24]
sortArray(A1), sortArray(A2)
m, n = len(A1), len(A2)
intersectionOfArrays(A1, A2, m, n)