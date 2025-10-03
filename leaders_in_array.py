def find_leaders(arr):
    n = len(arr)
    leaders = []
    for i in range(n-1):
        is_leader = True
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                is_leader = False
                break
        if is_leader:
            leaders.append(arr[i])
    leaders.append(arr[n-1])
    return leaders
arr = [5, 9, 7, 24, 16, 3, 1, 4, 10, 8]
result = find_leaders(arr)
print("Leaders in the array:", result)