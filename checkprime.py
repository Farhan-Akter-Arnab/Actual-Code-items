from math import sqrt
number = int(input("Enter a number: \n"))
if number > 1:
    if number != 2 and number % 2 == 0:
        print(number, " is not a prime number.")
    else:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                print(number, " is not a prime number.")
                break
        else:
            print(number, " is a prime number.")
else:
    print(number, " is not a prime number.")