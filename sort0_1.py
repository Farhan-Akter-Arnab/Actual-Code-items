def sortZeroOne(A,n):
    
    # Count the number of zeroes in the array
    count = 0
    
    for i in range(n):
        if A[i] == 0:
            count += 1
    # Filling the array with 0 until count
    for i in range(count):
        A[i] = 0
    # Filling the remaining array space with 1
    for i in range(count, n):
        A[i] = 1
    
    return A

# Driver Code
A = [0, 1, 0, 1, 1, 1]
n = len(A)
sortZeroOne(A, n)
print("Sorted Array is: ", end=" ")
for i in range(0,n):
    print(A[i], end=" ")