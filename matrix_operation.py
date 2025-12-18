def matrix_operation(X, Y, operation):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if operation == 'multiply':
        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]
        return result
    else:
        for i in range(len(X)):
            for j in range(len(X[0])):
                if operation == 'add':
                    result[i][j] = X[i][j] + Y[i][j]
                elif operation == 'subtract':
                    result[i][j] = X[i][j] - Y[i][j]
        return result
print("\nOperations of a 3x3 matrix\n")
print("For first matrix: ")
a, b, c = map(int, input("Enter 3 elements of first row separated by space: ").split()); d, e, f = map(int, input("Enter 3 elements of second row separated by space: ").split()); g, h, i = map(int, input("Enter 3 elements of third row separated by space: ").split()) # input for first matrix
print("\nFor second matrix: ")
j, k, l = map(int, input("Enter 3 elements of first row separated by space: ").split()); m, n, o = map(int, input("Enter 3 elements of second row separated by space: ").split()); p, q, r = map(int, input("Enter 3 elements of third row separated by space: ").split()) # input for second matrix
X = [[a, b, c], [d, e, f], [g, h, i]]; Y = [[j, k, l], [m, n, o], [p, q, r]] # defining matrices
added = matrix_operation(X, Y, 'add'); subtracted = matrix_operation(X, Y, 'subtract'); multiplied = matrix_operation(X, Y, 'multiply') # performing operations
print(added, "\n\n", subtracted, "\n\n", multiplied, "\n\n") # printing results