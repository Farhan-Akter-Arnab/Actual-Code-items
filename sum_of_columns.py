# initialising matrices

x = [[8, 2, 4],
     [4, 1, 9],
     [1, 4, 8]]

# initialising answer

answer = 0

# iterating through rows

for i in range(len(x)):

# iterating through columns
    
    for j in range(len(x[0])):
        # transpose matrix and add columns
        answer = answer + x[j][i]
        
    # Printing sum of each column
    print(answer, end=" , ")
    
    answer = 0