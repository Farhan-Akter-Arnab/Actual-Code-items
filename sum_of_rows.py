def matrix_sum_colrow(X, func):
    ans = 0
    list_row = []; list_col = []
    answer = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if func == 'row':
        for i in range(len(X)):
            for j in range(len(X[0])):
                ans = ans + X[i][j]
            list_row.append(ans); ans = 0
        return list_row
    elif func == 'col':
        for i in range(len(X)):
            for j in range(len(X[0])):
                ans = ans + X[j][i]
            list_col.append(ans); ans = 0
        return list_col
    elif func == 'transpose':
        for i in range(len(X)):
            for j in range(len(X[0])):
                answer[j][i] = X[i][j]
        return answer
a, b, c, d = map(int, input("Enter four integers for the first row separated by spaces: ").split()); e, f, g, h = map(int, input("Enter four integers for the second row separated by spaces: ").split()); i, j, k, l = map(int, input("Enter four integers for the third row separated by spaces: ").split()); m, n, o, p = map(int, input("Enter four integers for the fourth row separated by spaces: ").split())
X = [[a, b, c, d], [e, f, g, h], [i, j, k, l], [m, n, o, p]]; row_sum = matrix_sum_colrow(X, 'row'); col_sum = matrix_sum_colrow(X, 'col'); transpose_matrix = matrix_sum_colrow(X, 'transpose')
print("\nSum of each row:", row_sum, "\nSum of each column:", col_sum, "\nTranspose of the matrix:", transpose_matrix)