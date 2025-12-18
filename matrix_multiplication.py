# Initialising matrices

x = [[8, 2],
     [4, 1]]
y = [[3, 8],
     [9, 15]]

answer = [[0, 0],
        [0, 0]]

# Iterating through rows of X

for i in range(len(x)):
    
    for j in range(len(y[0])):
        
        for k in range(len(y)):
            answer[i][j] += x[i][k] * y[k][j]

# Printing answer
            
print(answer)
for r in answer:
    print(r)