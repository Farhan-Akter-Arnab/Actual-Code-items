def subset_sum(set_elements, target_sum):
    n = len(set_elements)
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True  # A sum of 0 can always be achieved with an empty subset
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if set_elements[i - 1] <= j: dp[i][j] = dp[i - 1][j] or dp[i - 1][j - set_elements[i - 1]]
            else: dp[i][j] = dp[i - 1][j]
    if not dp[n][target_sum]: return False, []  # No subset found that sums to target_sum
    subset = []    # Backtrack to find the subset
    i, j = n, target_sum
    while i > 0 and j > 0: # If current element came from the row above, it means it was not included in the subset
        if dp[i - 1][j]: i -= 1
        else: # Element was included in the subset
            subset.append(set_elements[i - 1])
            j -= set_elements[i - 1]; i -= 1
    subset.reverse()  # Reverse to maintain the original order
    return True, subset
set_elements = [3, 34, 4, 12, 5, 2]
target_sum = 24
exists, subset = subset_sum(set_elements, target_sum)
if exists: print(f"A subset with the target sum {target_sum} exists: {subset}")
else: print(f"No subset with the target sum {target_sum} exists.")