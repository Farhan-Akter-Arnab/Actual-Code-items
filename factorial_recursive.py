def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
n = int(input("Enter a non-negative integer: "))
result = factorial_recursive(n) if n >= 0 else "Invalid Input"
print(f"The factorial of {n} is: {result}; i.e. {n}! = {result}")