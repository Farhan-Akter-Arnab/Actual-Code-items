def divide(n, max_value=None):
    if max_value == None:
        max_value = n
    if n == 0:
        return [[]]
    if n < 0:
        return []
    partitions = []
    for i in range(min(n, max_value), 0, -1):
        for p in divide(n - i, i):
            partitions.append([i] + p)
    return partitions
n = int(input("Enter a positive integer: "))
partitions = divide(n)
print(partitions)
print("Number of ways to divide", n, ":", len(partitions))