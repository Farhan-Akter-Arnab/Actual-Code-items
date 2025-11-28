# Programme to check if the given array is sorted and rotated
arr = [3, 4, 5, 1, 2]
n= len(arr)
cnt = 0
count = 0

# iterating loop from 1 to length of array
for i in range(1, n):
    # checking if previous element is greater than current element
    if arr[i-1] > arr[i]:
        cnt += 1

# special case: checking if last element is greater than first element
if arr[n-1] > arr[0]:
    count += 1
    
# driver code
print("\nGiven array is:", arr)
if cnt <= 1:
    print("Array is sorted and rotated")
if count > 0:
    print("Array is not rotated")
else:
    print("Array is rotated")