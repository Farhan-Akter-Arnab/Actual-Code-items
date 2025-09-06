def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
X = int(input("Enter integer value for X to calculate factorial: "))
result = factorial(X)
print(X, "! = ", result)