# Python program to find the length of the longest common subsequence
def lcs(X, Y, m, n):
    # Declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]
    # Building the L table in bottom-up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    # Returning the length of the longest common subsequence
    return L[m][n]

# Driver code
if __name__ == "__main__":
    X = input("Enter first string: ")
    Y = input("Enter second string: ")
    m = len(X)
    n = len(Y)
    print("Length of LCS is", lcs(X, Y, m, n))