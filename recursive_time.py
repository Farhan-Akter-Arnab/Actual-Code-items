def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
A = int(input("Enter the number to calculate the factorial of: "))
print(A,"! = ", factorial(A))
print("Time complexity: O(n)")
def Print(n, a):
    if n > a:
        return
    print(n)
    Print(n + 1, a)
W = int(input("Enter the upper limit: "))
Print(1, W)
print("Time complexity: O(n)")