#Calculating circumference of a circle
r = float(input("Enter radius: "))
def circle_circumference(r):
    return 2 * 3.141592653589793238462643383 * r
print(circle_circumference(r)) #here one has to input value of r as a number
def circle_area(r):
    return 3.141592653589793238462643383 * (r**2)
print(circle_area(r))