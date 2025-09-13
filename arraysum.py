def arrayTotalSum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arrayTotalSum(a[1:])
a = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print("The sorted array is: ", sorted(a))
print("The sum of the array elements is:", arrayTotalSum(a))