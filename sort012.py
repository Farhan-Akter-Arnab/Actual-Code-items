def sort012(a,n):
    low = 0
    mid = 0
    high = n -1
    
    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a

a = [1, 1, 0, 2, 1, 2, 0, 0, 2, 1, 1, 0, 2, 0, 1, 2, 0, 1, 1, 2, 0, 0, 1, 1]
n = len(a)
print("Original Array: ")
print(a)
sort012(a, len(a))
print("Array after sorting 0, 1 and 2 : ")
print(a)