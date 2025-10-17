def find_equilibrium_index(arr):
    
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        total_sum -= arr[i]
        
        if left_sum == total_sum:
            return i
        
        left_sum += arr[i]
    
    return -1

# Example Usage
arr = [1, 3, 6, 2, 2]
index = find_equilibrium_index(arr)

if index != -1:
    print("Equilibrium index is: ", index)
    
else:
    print("No equilibrium index found")