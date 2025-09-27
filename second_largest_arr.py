def second_largest(arr, size):
    first = second = 0
    for i in range(size):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif (arr[i] > second and arr[i] != first):
            second = arr[i]
    if second == 0:
        print("There is no second largest element.")
    else:
        print("The second largest element is:", second)
arr = [12, 24, 97, 80, 60, 24]
size = len(arr)
second_largest(arr, size)