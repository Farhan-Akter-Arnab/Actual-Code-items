def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def nCr(n, r):
    if r > n:
        return 0
    return factorial(n) / (factorial(r) * factorial(n - r))
def paths(n, m):
    return nCr(n + m - 2, m - 1)

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print("Number of unique paths from top-left to bottom-right:", int(paths(r, c)))