# Shell sort in Python
A = [9, 8, 3, 7, 5, 6, 4, 1]
print("Original array is:")
print(A)
# initialising n
n = len(A)
# Rearrange elements at each n/2, n/4, ... intervals
interval = n // 2

while interval > 0:
    for i in range(interval, n):
        temp = A[i]
        j = i
        while j >= interval and A[j - interval] > temp:
            A[j] = A[j - interval]
            j -= interval
        A[j] = temp
    interval //= 2

# Driver Code
print("Sorted array is:")
print(A)
print("Time Complexity: O(n log n) on average")
print("Space Complexity: O(1)")