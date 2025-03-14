def FACTORIAL(n):
    if n == 0 or n == 1: #Base case: 0! and 1! both equal to 1
        return 1
    else:
        return n * FACTORIAL(n-1) #Recursive call
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("The factorial of ", num, " is ", FACTORIAL(num))