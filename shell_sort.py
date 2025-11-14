# Shell sort in Python
def shell_sort(arr):
    # initialsing n
    n = len(arr)
    # Rearranging elements at each n/2, n/4, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2
    return arr

# Driver code
if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Your Unsorted array:", arr)
    shell_sort(arr)
    print("Sorted array:")
    print(arr)