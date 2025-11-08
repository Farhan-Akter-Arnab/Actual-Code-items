# Program for Insertion Sort

A = [10, 5, 13, 8, 2]
print("Given array is: ")
print(A)

# traverse through the array
for i in range(1, len(A)):
    value = A[i]
    # Move elements of A[0,...i-1], that are
    # greater than value, to one position ahead
    # of their current position
    
    j = i - 1
    while j >= 0 and A[j] > value:
        A[j + 1] = A[j]
        j -= 1
        A[j + 1] = value

# Driver code
print("Sorted array is: ")

for i in range(len(A)):
    print("%d" % A[i], end=", ")