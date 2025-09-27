def arraymean(arr, arr_size):
    total_sum = 0
    for i in range(0, arr_size):
        total_sum += arr[i]
    return float(total_sum / arr_size)

def arraygeomean(arr, arr_size):
    product = 1.0
    for i in range(0, arr_size):
        product *= arr[i]
    return float(product ** (1.0 / arr_size))

def arraymedian(arr, arr_size):
    sorted(arr)
    if arr_size % 2 != 0:
        return float(arr[int(arr_size / 2)])
    return float((arr[int((arr_size - 1) / 2)] + arr[int(arr_size / 2)]) / 2.0)

arr = [2, 4, 6, 8, 10, 12, 16, 18, 20, 24]
arr_size = len(arr)

print("Arithmetic Mean = ", arraymean(arr, arr_size))
print("Geometric Mean = ", arraygeomean(arr, arr_size))
print("Median = ", arraymedian(arr, arr_size))