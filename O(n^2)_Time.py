def test(n):
    iteration = 0
    for a in range(0, n):
        for w in range(0, n):
            print("*", end="")
            iteration += 1
        print("")
    print("\nWhen n = ", n, ", iterations = ", iteration)
test(8)
test(10)
test(24)
print("\nWith every 'n' time taken = n^2 ")
print("Time Complexity = O(n^2)")