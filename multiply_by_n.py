def f(m,n):
    print("Time complexity: constant (1)")
    return m * n
def g(m,n):
    print("Time complexity: linear (n)")
    result = 0
    for i in range(m):
        result += n
        print("Intermediate result:", result)
    return result
print(f(8,3)) # returns 24
print(g(8,3)) # returns 24