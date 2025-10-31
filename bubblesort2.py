# This function implements the Bubble Sort algorithm to sort a list of numbers in ascending order.
def BubbleSort(arr):
    n = len(arr)
    count = 0
    # Traverse through the array
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                count +=1
                print("Iteration: {} at step {}".format(arr, count))
            # If no two elements were swapped by inner loop, then break
        if swap ==  False:
            break
    return arr
# Driver code
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
BubbleSort(arr)
print("Sorted array: ")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")