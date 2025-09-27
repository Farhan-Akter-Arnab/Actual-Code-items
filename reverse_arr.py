def reverse(arr):
    A = []
    while len(arr) > 0:
        A.append(arr[-1])
        arr.pop()
    return A
array = list(map(int,input("Enter the elements of the array separated by spaces: ").split()))
print("Reversed array:", reverse(array))