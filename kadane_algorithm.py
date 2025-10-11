# Programme to find maximum subarray sum using Kadane's Algorithm

def maxsubarraysum(a, a_size):
    max = -float('inf')
    cmax = 0
    a_size = len(a)
    
    # Add current element to current max, check if it is greater than max. If yes, update max.
    # If current max becomes negative, set it to 0.
    for i in range(0, a_size):
        cmax = cmax + a[i]
        if max < cmax:
            max = cmax
            print("Updated max:", max)
        
        if cmax < 0:
            cmax = 0
            
    return max

a = [1, 2, 3, -4, 6, -22, -4, 22, -9, 11]
print("Original Array : ", a)
sum = maxsubarraysum(a, len(a))
print("Maximum contiguous sum is = ", sum)