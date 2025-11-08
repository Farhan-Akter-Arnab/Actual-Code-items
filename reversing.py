# Program to reverse the same array

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

def reverse_array(arr):
    n = len(arr)
    
    # initialising start and end
    start = 0
    end = n -1
    
    while start < end:
        # swapping the elements of an array
        # to reverse it in the same array
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
# Driver Code
reverse_array(A)
print("Reversed array is : ")

for i in range(len(A)):
    print("%d" % A[i], end = ' ')