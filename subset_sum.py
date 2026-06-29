def is_subset_sum(arr, target):
    n = len(arr)
    # dp[j] will be True if there is a subset of arr[] with sum j
    dp = [False] * (target + 1)
    
    # A subset with sum 0 is always possible (the empty subset)
    dp[0] = True
    
    for i in range(n):
        for j in range(target, arr[i] - 1, -1):
            if dp[j - arr[i]]:
                dp[j] = True
                
    return dp[target]

# Example usage:
arr = [3, 34, 4, 12, 5, 2]
target = 24
print(is_subset_sum(arr, target))