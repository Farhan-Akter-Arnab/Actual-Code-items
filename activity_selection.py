# Activity Selection Problem
# Given n activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

def printMaxActivities(start, finish):
    
    n = len(finish)
    print("The following activities are selected:")
    i = 0
    print(i, end=' ')
    
    for j in range(1, n):
        
        if start[j] >= finish[i]:
            print(j, end=' ')
            
            i = j

# Driver code
if __name__ == "__main__":
    
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    # Function call
    printMaxActivities(start, finish)