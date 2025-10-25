def isPairSum(A, N, X):

  for i in range(N):
    for j in range(N):

      # As equal i and j means same element
      if (i == j):
        continue

      # Pair exists
      if (A[i] + A[j] == X):
        return [A[i], A[j]]
      
      # As the array is sorted
      if (A[i] + A[j] > X):
        break

  # No pair found with given sum
  return 0

# Driver code
arr = [2,3,5,8,9,10,11]
val = 17
print("Pairs with sum equal to {} = {}".format(val, isPairSum(arr, len(arr), val)))
