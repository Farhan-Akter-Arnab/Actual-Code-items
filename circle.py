import math
class circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def circumference(self):
        return 2 * math.pi * self.r
radius = float(input("Enter the radius of the circle: "))
print("The circumference of your circle is: ", circle(radius).circumference())
print("The area of your circle is: ", circle(radius).area())