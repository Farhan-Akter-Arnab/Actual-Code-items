# initialising matrices

x = [[8, 2, 4],
     [4, 1, 9],
     [1, 4, 8]]

# initialising answer matrix with zeros
answer = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# transposing matrix
for i in range(len(x)):
    for j in range(len(x[0])):
        # transposing matrix
        answer[j][i] = x[i][j]

# Printing answers
        
print("Transposed matrix is: ")
print(answer)
        
for r in answer:
    print(r)