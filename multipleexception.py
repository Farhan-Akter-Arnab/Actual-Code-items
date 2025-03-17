try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Result is = ", result)
    print("Result is = ", result1)
except ZeroDivisionError:
    print("Division by zero is not allowed [undefined]")
except ValueError:
    print("Please enter numerical value")
except NameError as ex:
    print("The exception is = ", ex)
except:
    print("Some error occurred")
finally:
    print("I will execute no matter what happens")