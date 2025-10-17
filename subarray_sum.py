def subarray_with_sum(arr, target_sum):
    curr_sum = 0
    start = 0
    
    for end in range(len(arr)):
        curr_sum += arr[end]
        
        # Remove elements from start if current sum exceeds target
        while curr_sum > target_sum and start < end:
            curr_sum -= arr[start]
            start += 1
            
        # Check if we found the subarray
        if curr_sum == target_sum:
            print("Subarray found from index ", start, " to ", end)
            print("Subarray : ", arr[start:end+1])
            return
        
    print("No subarray found with the given sum")
    
# Example usage
arr = [1, 2, 3, 3, 7, 5, 3]
target_sum = 24
subarray_with_sum(arr, target_sum)