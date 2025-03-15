a = input("Enter anything: ")
b = input("Enter a character which you want to check whether it is there or not: ")
for i in a: #iterate for loop
    if (i == b): #condition1
        #display result
        print(b, " is found")
        break #break statement
    else:
        #display result
        print(b, " is not found")