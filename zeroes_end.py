# Programme to move all the zeroes at the end
def pushzerotoend(a, a_size):
    
    # Zero will hold the position where the next zero is to be placed
    zero = 0
    
    # Nonzero will iterate through the array
    nonzero = 0
    
    while nonzero != a_size:
        # If the current element is non-zero
        if a[nonzero] != 0:
            # swap the elements at zero and nonzero index
            a[zero], a[nonzero] = a[nonzero], a[zero]
            zero += 1
        nonzero += 1 # always move the nonzero pointer forward        
    return a
# Driver code
a = [0, 1, 9, 8, 2, 0, 0, 4, 7, 0, 6, 0]
a_size = len(a)
print("Original array: ")
print(a)
print("Array after pushing all zeroes to the end of array: ")
print(pushzerotoend(a, a_size))