def min_coins(coinset, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for coin in coinset:
        for value in range(coin, target + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)
    return dp[target]
# Example usage:
coinset = [1, 2, 5, 8, 10, 20, 24, 48, 72, 80, 96, 100]
target = 1997
min_coins_needed = min_coins(coinset, target)
print("Minimum number of coins needed:", min_coins_needed)