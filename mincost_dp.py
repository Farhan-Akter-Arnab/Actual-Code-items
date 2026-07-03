# Dynamic Programming Python implementation of Min Cost Path problem
R = 3
C = 3
def minCost(cost, m, n):
    # Create a 2D array to store the cumulative cost
    total_cost = [[0 for x in range(C)] for x in range(R)]
    total_cost[0][0] = cost[0][0]
    # Initialize first column of total_cost array
    for i in range(1, m+1):
        total_cost[i][0] = total_cost[i-1][0] + cost[i][0]
    # Initialize first row of total_cost array
    for j in range(1, n+1):
        total_cost[0][j] = total_cost[0][j-1] + cost[0][j]
    # Fill the rest of the array
    for i in range(1, m+1):
        for j in range(1, n+1):
            total_cost[i][j] = min(total_cost[i-1][j-1], total_cost[i-1][j], total_cost[i][j-1]) + cost[i][j]
    return total_cost[m][n]
# Driver Code

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCost(cost, 2, 2))