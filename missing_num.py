def find_missing_number(arr, n):
    total = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total - arr_sum

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
n = int(input("Enter the number of elements: "))
print("The missing number is:", find_missing_number(arr, n))