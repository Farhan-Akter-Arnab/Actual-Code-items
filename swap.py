def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping: a =", a, "b =", b)
def swap2(a,b):
    a = (a & b) + (a | b)
    b = a + ~b + 1
    a = a + ~b + 1
    print("After swapping: a =", a, "b =", b)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
swap(x,y)
swap2(x,y)