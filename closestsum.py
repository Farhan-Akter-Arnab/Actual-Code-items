def printClosest(arr, n, x):
    l = 0
    r = n -1
    diff = float('inf')
    res_l = 0
    res_r = 0
    while (l < r):
        current_sum = arr[l] + arr[r]
        if abs(x - current_sum) < diff:
            res_l = l
            res_r = r
            diff = abs(current_sum - x)
        if current_sum > x:
            r -= 1
        else:
            l += 1
    print("The closest pair to sum {} is {} and {}".format(x, arr[res_l], arr[res_r]))

# Driver code to test above function
if __name__ == "__main__":
    arr = [10, 24, 28, 28, 29, 40]
    n = len(arr)
    x = 54
    printClosest(arr, n, x)