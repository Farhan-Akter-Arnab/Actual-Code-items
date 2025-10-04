def max_min_difference(arr, arr_size):
    if not arr:
        return 0
    max = 0
    min = float('inf')
    for i in range(arr_size):
        if arr[i] > max:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]
    print("Maximum element is:", max)
    print("Minimum element is:", min)
    return max - min
array = [72, 85, 97, 24, 90, 63, 45, 40, 8, 10]
difference = max_min_difference(array, len(array))
print("Difference between max and min is:", difference)