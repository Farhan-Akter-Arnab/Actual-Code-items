# Program to find out the number of shifts required to sort an array using insertion sort
def insertion(arr):
    n = len(arr)
    shifts = 0
    # Traverse through 1 to n
    for i in range(1, n):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
            arr[j + 1] = key
    # Return the sorted array and the number of shifts
    return arr, shifts

# Example usage
if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    print("Original array:", arr)
    sorted_arr, total_shifts = insertion(arr)
    print("Sorted array:", sorted_arr)
    print("Total shifts required:", total_shifts)