#importing math library
import math

#taking user input
angle = float(input("Enter the angle in degrees: "))
#converting degrees to radians
theta = angle*(3.141592653589793238462643383)/180

#configuring the values of sine, cosine and tangent of the angle
sine = math.sin(theta)
cosine = math.cos(theta)
tangent = math.tan(theta)

#configuring the values of cotangent, secant and cosecant of the angle
cotangent = 1 / tangent
secant = 1 / cosine
cosecant = 1 / sine

print("sin(your angle) = ", sine)
print("cos(your angle) = ", cosine)
print("tan(your angle) = ", tangent)
print("cot(your angle) = ", cotangent)
print("sec(your angle) = ", secant)
print("cosec(your angle) = ", cosecant)