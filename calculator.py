def add (x,y):
    return x + y
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x,y):
    return x / y
def exp (x,y):
    return x ** y
def mod (x,y):
    return x % y

print("Choose what you want to find out for two numbers: ")
print("\na. Addition")
print("\nb. Subtraction")
print("\nc. Multiplication")
print("\nd. Division")
print("\ne. Exponentiation")
print("\nf. Remainder")
print("For writing input, please type only a/b/c/d/e/f")
choice = input("Choose from the above six: ")

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

if choice == "a":
    print(n1 , " + " , n2 , " = ", add(n1,n2))
elif choice == "b":
    print(n1 , " - " , n2 , " = ", subtract(n1,n2))
elif choice == "c":
    print(n1 , " x " , n2 , " = ", multiply(n1,n2))
elif choice == "d":
    print(n1 , " / " , n2 , " = ", divide(n1,n2))
elif choice == "e":
    print(n1 , " ^ " , n2 , " = ", exp(n1,n2))
elif choice == "f":
    print(n1 , " == " , mod(n1,n2) , " mod " , n2)
else:
    print("INVALID INPUT")