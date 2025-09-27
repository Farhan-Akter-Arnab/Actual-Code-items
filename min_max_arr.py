def minimum(arr, size):
    temp = arr[0]
    for i in range(1, size):
        temp = min(temp, arr[i])
    return temp
def maximum(arr, size):
    temp = arr[0]
    for i in range(1, size):
        temp = max(temp, arr[i])
    return temp
arr = [8, 10, 12, 16, 24]
size = len(arr)
print("Minimum element is:", minimum(arr, size))
print("Maximum element is:", maximum(arr, size))