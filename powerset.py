import math

def printPowerSet(set, SetSize):
    PowerSetSize = (int)(math.pow(2, SetSize))
    outer = 0
    inner = 0
    
    for outer in range(0, PowerSetSize):
        for inner in range(0, SetSize):
            if((outer & (1 << inner)) > 0):
                print(set[inner], end= ", ")
        print("\n")
        
size = int(input("Enter the size of the set: "))
set = []

for i in range(0, size):
    n = int(input("Enter element: "))
    set.append(n)
    
    if set == []:
        print("Ø")
        
printPowerSet(set, len(set))