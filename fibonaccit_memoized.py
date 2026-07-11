# This is a simple implementation of the Fibonacci sequence using memoization to optimize the recursive calls.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Memoized version
def fibonacci_memoized(n):
    memo = {}
    def _fibonacci(n):
        if n in memo:
            return memo[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            memo[n] = result
            return result
    return _fibonacci(n)

# Driver code to test the function
num = int(input("Enter a number: "))
print(fibonacci_memoized(num))