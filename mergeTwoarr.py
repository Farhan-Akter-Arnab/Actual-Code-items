def mergeTwoArrays(A1, A2, m, n):
    A3 = [None] * (m + n)
    i = j = k = 0
    while i < m and j < n:
        if A1[i] < A2[j]:
            A3[k] = A1[i]
            i += 1
        else:
            A3[k] = A2[j]
            j += 1
        k += 1
    while i < m:
        A3[k] = A1[i]
        i += 1
        k += 1
    while j < n:
        A3[k] = A2[j]
        j += 1
        k += 1
    print("Merged Arrays: ")
    for i in range(m + n):
        print(A3[i], end=" ")
A1 = [2, 4, 6, 8, 10]
A2 = [12, 16, 18, 20, 24]
m, n = len(A1), len(A2)
mergeTwoArrays(A1, A2, m, n)