# 0-1 Knapsack Problem using Memoization
def knapsackRec(W, val, wt, n, memo):
    if n == 0 or W == 0:
        return 0
    if memo[n][W] != -1:
        return memo[n][W]
    pick = 0
    
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1, memo)
    notPick = knapsackRec(W, val, wt, n - 1, memo)
    memo[n][W] = max(pick, notPick)
    return memo[n][W]

def knapsack(W, val, wt):
    n = len(val)
    memo = [[-1] * (W + 1) for _ in range(n + 1)]
    return knapsackRec(W, val, wt, n, memo)

if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4
    print(knapsack(W, val, wt))