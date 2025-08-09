def isEvenOdd(n):
    if (n ^ 1 == n + 1):
        return True
    else:
        return False
number = int(input("Enter a number: "))
if isEvenOdd(number):
    print(number, " is even.")
else:
    print(number, " is odd.")