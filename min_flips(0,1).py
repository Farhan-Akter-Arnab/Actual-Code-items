def min_flips(arr):
    n = len(arr)
    flip = []
    for i in range(1,n):
        if arr[i] != arr[0]:
            if arr[i] != arr[i-1]:
                flip.append((i,i))
            elif flip and flip[-1][1] == i-1:
                flip[-1] = (flip[-1][0], i)
    print("Number of flips required:", len(flip))
    print("Flip segments: ", flip)
array = [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1]
print("Input array:", array)
min_flips(array)