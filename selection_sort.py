def selection_sort(arr):
    n = len(arr)
    count = 0
    
    for i in range(n):
        min_id = i
        
        for j in range(i+1, n):
            if arr[min_id] > arr[j]:
                min_id = j
            count += 1    
        
        arr[i], arr[min_id] = arr[min_id], arr[i]
        print("After {} iterations, the array is: {}".format(count, arr))    
    
    return arr

# Driver code
if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    selection_sort(arr)
    print("The sorted array: ")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")