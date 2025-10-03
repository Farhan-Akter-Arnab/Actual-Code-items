def reverse_in_groups(arr,n):
    for i in range(0, len(arr), n):
        start = i
        end = min(i + n - 1, len(arr) - 1)
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return arr
arr = list(map(int, input("Enter the elements of your array (space-separated): ").split()))
n = int(input("Enter the group size for reversal: "))
print("Original array:", arr)
result = reverse_in_groups(arr, n)
print("Array after reversing in groups of", n, ":", result)