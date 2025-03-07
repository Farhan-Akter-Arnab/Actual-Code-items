def circle_perimeter(r):
    return 2 * r * 3.141592653589793238462643383
def rectangle_perimeter(l,b):
    return 2*(l + b)
def triangle_perimeter(a,b,c):
    return a+b+c
def square_perimeter(s):
    return 4*s

print("Please select shape for calculating the perimeter: ")
print("a. Circle")
print("b. Rectangle")
print("c. Triangle")
print("d. Square")
choice = input("Please enter the choice (a/b/c/d/...): ")

if choice == 'a':
    r = float(input("Please enter the radius: "))
    print("The perimeter of your shape is = ", circle_perimeter(r))
elif choice == 'b':
    length = float(input("Please enter the length: "))
    breadth = float(input("Please enter the breadth: "))
    print("The perimeter of your shape is = ", rectangle_perimeter(length,breadth))
elif choice == 'c':
    a = float(input("Please enter the first side: "))
    b = float(input("Please enter the second side: "))
    c = float(input("Please enter the third side: "))
    print("The perimeter of your shape is = ", triangle_perimeter(a,b,c))
elif choice == 'd':
    side = float(input("Please enter length of one side: "))
    print("The perimeter of your shape is = ", square_perimeter(side))
else:
    print("Invalid Input")