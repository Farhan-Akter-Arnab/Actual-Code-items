def unique_paths_with_obstacles(grid):
    m = len(grid)
    n = len(grid[0])
    if grid[0][0] == 1:
        return 0 
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 # Base case  
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue             
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                ways_from_top = dp[i-1][j] if i > 0 else 0
                ways_from_left = dp[i][j-1] if j > 0 else 0               
                dp[i][j] = ways_from_top + ways_from_left                
    return dp[m-1][n-1]
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(unique_paths_with_obstacles(grid))  # Output: 2