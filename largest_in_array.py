def MaxElementArray(a):
    length = len(a)
    if length == 1:
        return a[0]
    return max(a[0], MaxElementArray(a[1:]))

a = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print("The largest element in the array is:", MaxElementArray(a))