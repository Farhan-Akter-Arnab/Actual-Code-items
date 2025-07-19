def potato(n):
    print("\nTime complexity: O(n): Linear")
    for i in range(0, n+1):
        print("First loop iteration:", i)
    j = 1
    print("\nTime complexity: O(log n): Logarithmic")
    while (j < n+1):
        print("Second loop iteration:", j)
        j = j * 2
    print("\nTime complexity: O(1): Constant")
    for i in range(0,100):
        print("Third loop iteration:", i)
potato(10240808242424240824)