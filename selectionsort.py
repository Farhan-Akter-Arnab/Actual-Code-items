# Program for selection sort
def selection_sort(arr):
    
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining array
        min_id = i
        
        for j in range(i+1, n):
            if arr[min_id] > arr[j]:
                min_id = j
        # Swap the found minimum element
        # with the first element
        arr[i], arr[min_id] = arr[min_id], arr[i]
        
    return arr

# Driver code
A = [64, 24, 12, 10, 11, 8, 9]
selection_sort(A)

print("Sorted array is: ")
for i in range(len(A)):
    print("%d" % A[i],end=" ")