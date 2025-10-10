
def getmaxlength(a, a_size):
    
    counter = 0
    
    maxones = 0
    
    for i in range(0, a_size):
    
        if (a[i] == 0):
    
            counter = 0
    
        else:
    
            counter += 1
            maxones = max(maxones, counter)
    
    return maxones

a = [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
a_size = len(a)

print("Maximum number of 1s = ", getmaxlength(a, a_size))