# This function calculates the minimum number of coins needed to make a given amount using a list of coin denominations.

def coin_change(coins, amount):
    # Initialize a list to store the minimum number of coins needed for each amount from 1 to the target amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Solve subproblems for each amount from 1 to the target.
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    else:
        return dp[amount]

# Example usage:
coins = [1, 2, 5, 10, 20, 50, 60, 80, 100, 120]
amount = 824
result = coin_change(coins, amount)
print(f"The minimum number of coins needed to make {amount} is: {result}")