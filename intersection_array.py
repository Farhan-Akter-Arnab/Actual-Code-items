# Python Programme to find the intersection of two arrays
# initialising two arrays
A1 = [1, 2, 3, 4, 5, 6, 8, 10]
A2 = [2, 3, 5, 7, 8, 9, 10, 15]
print("The original arrays are: ")
print(A1)
print(A2)
print("The intersection of the two arrays is: ")
# initialising m and n
m = len(A1)
n = len(A2)
i, j = 0, 0

while i < m and j < n:
    # Comparing array items
    if A1[i] < A2[j]:
        i += 1
    elif A2[j] < A1[i]:
        j += 1
    else:
        # printing the intersection item of both the arrays
        print(A1[i], end=" ")
        i += 1
        j += 1