def maxproduct(arr):
    n = len(arr)
    if n < 2:
        return None
    
    max = float('-inf')
    n1 = 0
    n2 = 0
    
    for i in range (0, n):
        new_product = float(arr[i] * arr[i+1])
        if new_product > max:
            max = new_product
            print("Numbers giving max product: ", arr[i], arr[i+1])
            n1, n2 = arr[i], arr[i+1]
            print("Maximum product right now: = ", max)
        if i == n-2:
            break
    
    print("\nNumbers giving final max product: ", n1, n2)
    print("Final Maximum product is: ", max, "\n")

a = list(map(int, input("Enter the numbers separated by spaces: ").split()))
maxproduct(a)