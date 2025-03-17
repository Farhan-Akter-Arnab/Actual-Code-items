try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("The outcome is = ", result)
    print("The outcome is = ", r)
    open("Actual Code items", 'a+w')
except ArithmeticError as ex:
    print("Exception: ", ex)
except ValueError as ex:
    print("Please enter integer numbers: ")
except ZeroDivisionError as ex:
    print("Number divided by zero is undefined")
except NameError as ex:
    print("Exception: ", ex)