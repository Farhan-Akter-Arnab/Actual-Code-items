def count_paths(maze):
    rows = len(maze)
    cols = len(maze[0])
    if maze[0][0] == 0 or maze[rows - 1][cols - 1] == 0:
        return 0
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = 1
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 0:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    return dp[rows - 1][cols - 1]

maze = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
print("Number of ways: ", count_paths(maze))