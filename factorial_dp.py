def factorial_dp(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]
n = int(input("Enter a non-negative integer: "))
result = factorial_dp(n) if n >= 0 else "Invalid Input"
print(f"The factorial of {n} is: {result}; i.e. {n}! = {result}")