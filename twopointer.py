def isPairSum(A, N, X):
    # represents the first pointer
    i = 0
    # represents the second pointer
    j = N - 1
    while (i < j):
        # If we find a pair
        if (A[i] + A[j] == X):
            return (A[i], A[j])
        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i+=1
        elif (A[i] + A[j] < X):
            i += 1
        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j-=1
        else:
            j -= 1
    return 0
arr = [1,3,7,8,9,10,11,24]
# Value to search
value = 17
print("Pair with the sum equal to {} is = {}".format(value, isPairSum(arr, len(arr), value)))