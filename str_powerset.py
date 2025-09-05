import math

def str_powerset(x):
    str_size = len(x)
    outer = 0
    inner = 0
    
    for outer in range(0, int(math.pow(2, str_size))):
        Empty_Set = True
        for inner in range(0, str_size):
            if (outer & (1 << inner)) > 0:
                print(x[inner], end="")
                Empty_Set = False
        
        if Empty_Set:
            print("Ø", end="")
        print(" ")
    return

string = str(input("Enter something: "))
set = []
for i in range(0, len(string)):
    set.append(string[i])
str_powerset(set)