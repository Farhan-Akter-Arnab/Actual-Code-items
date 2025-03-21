L = [49, 34, 54, 35, 24, 80, 88, 96, 48, 16, 12, 20, 72, 42, 32, 10, 64, 29, 25, 50, 90, 16, 84, 40]
print("Original list: ", L)
count = 0
# Finding the sum
for i in L:
    count += i
mean = count/len(L)
print("Sum = ", count)
print("Arithmetic Mean = ", mean)
# Sorting the element of the list
L.sort()
# Printing the first element
print("Smallest element is: ", L[0])
# Printing the last element
print("Largest element is: ", L[-1])