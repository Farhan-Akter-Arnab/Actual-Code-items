def BubbleSort(arr):
    n = len(arr)
    # Traverse through the array
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element
            # found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
            # If no two elements were swapped
            # by inner loop, then break
            if swap == False:
                break
            
# Driver code
arr = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(arr)
print("Sorted array : ")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")