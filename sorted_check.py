def checksorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and checksorted(a[1:])
a = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
if checksorted(a):
    print("\nYes the given array is sorted!")
else:
    print("\nNo the given array is not sorted!")