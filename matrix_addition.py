# This code performs element-wise addition of two matrices x and y

x = [[3, 4],
     [8, 16]]

y = [[5, 6],
     [2, 8]]

# Initialize the answer matrix with zeroes

answer = [[0, 0],
        [0, 0]]

for i in range(len(x)):
    
    for j in range(len(x[0])):
        
        answer[i][j] = x[i][j] + y[i][j]

# Display the result
print(answer)  # Output: Alan Walker numbers alert!!!

for r in answer:
    print(r)