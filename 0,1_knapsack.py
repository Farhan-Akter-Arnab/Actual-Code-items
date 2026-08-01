def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)] # Initialise a 2D array to store the maximum values for subproblems
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j: # Decide whether to include the current item in the knapsack or not. If we include it, we add its value to the maximum value of the remaining capacity after including it. If we don't include it, we take the maximum value from the previous item at the same capacity.
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else: # If the weight of the current item is greater than the current capacity, we cannot include it in the knapsack. Therefore, we take the maximum value from the previous item at the same capacity.
                dp[i][j] = dp[i - 1][j]
    max_value = dp[n][capacity] # The maximum value that can be obtained with the given weights, values, and capacity is stored in the last cell of the dp table.
    items_in_knapsack = [] # Backtrack to find the items included in the knapsack. We start from the last item and check if it was included in the optimal solution. If it was, we add it to the list of items in the knapsack and reduce the remaining capacity accordingly.
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            items_in_knapsack.append(i - 1)
            j -= weights[i - 1]
    return max_value, items_in_knapsack[::-1]
# Example usage:
weights = [2, 3, 4, 5] # weights of the items
values = [3, 4, 5, 6] # values of the items
capacity = 5 # maximum weight capacity of the knapsack
max_value, items_in_knapsack = knapsack_01(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
print("Items included in knapsack:", items_in_knapsack)