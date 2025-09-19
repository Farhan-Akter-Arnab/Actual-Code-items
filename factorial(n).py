# Calculating the factorial of a non-negative integer using recursion
def factorial(n):
    if n < 0 or type(n) != int:
        print("Error: We can calculate the factorials of only non-negative integers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a non-negative integer to calculate the factorial: "))
print(n,"! = ", factorial(n))