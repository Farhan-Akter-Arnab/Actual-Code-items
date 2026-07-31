def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    # Initialize a 2D array to store the edit distances
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # Initialize the first row and column of the array
    for i in range(m + 1):
        dp[i][0] = i # Initialize the first column
    for j in range(n + 1):
        dp[0][j] = j # Initialize the first row
    # Fill the rest of the array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] # No operation needed
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) # Insert, Delete, Replace
    return dp[m][n]

# Example usage
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = edit_distance(str1, str2)
print(f"The edit distance between '{str1}' and '{str2}' is: {result}")