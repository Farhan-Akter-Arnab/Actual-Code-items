l = int(input("Enter how many times will you repeat the loop: "))
for i in range(l):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a == b or a < b:
        print(a, " ", b)
    else:
        print(b, " ", a)