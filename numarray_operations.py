import numpy as np
numdata = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
print("\nOriginal array:", numdata)
print("Shape of the array:", numdata.shape)
numdata1 = np.where(numdata % 2 != 0, -1, numdata)
print("Array after replacing odd numbers with -1:", numdata1)
numdata2 = np.reshape(numdata, (2, 12))
print("Reshaped array to 2 rows and 12 columns:\n", numdata2)
numdata3 = np.reshape(numdata, (3, 8))
print("Reshaped array to 3 rows and 8 columns:\n", numdata2)
numdata4 = np.reshape(numdata, (4, 6))
print("Reshaped array to 4 rows and 6 columns:\n", numdata2)
numdata5 = np.reshape(numdata, (6, 4))
print("Reshaped array to 6 rows and 4 columns:\n", numdata2)
numdata6 = np.reshape(numdata, (8, 3))
print("Reshaped array to 8 rows and 3 columns:\n", numdata2)
numdata7 = np.reshape(numdata, (12, 2))
print("Reshaped array to 12 rows and 2 columns:\n", numdata2)
numdata8 = np.reshape(numdata, (24, 1))
print("Reshaped array to 24 rows and 1 column:\n", numdata2)
n = 0
for i in numdata:
    n += i
print("Sum of all elements in the array:", n)