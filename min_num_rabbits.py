def min_number_of_rabbits(answers, N):
    Map = {}
    for a in range(N):        
        if answers[a] in Map:
            Map[answers[a]] += 1    
        else:
            Map[answers[a]] = 1
    
    count = 0
    
    for a in Map:
        x = a
        y = Map[a]
        
        if (y % (x + 1)) == 0:
            count = count + ((y // (x + 1)) * (x + 1))
        else:
            count = count + ((y // (x + 1) + 1) * (x + 1))
    
    return count

arr = [2, 2, 0, 0]
N = len(arr)
print(min_number_of_rabbits(arr, N))