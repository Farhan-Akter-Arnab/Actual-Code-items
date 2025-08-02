a = int(input("\nEnter the first number: "))
w = int(input("Enter the second number: "))
def lcm(a,w):
    greater = max(a,w)
    a_w = 1
    while True:
        m = greater * a_w
        if m % a == 0 and m % w == 0:
            return m
        a_w += 1
print("\nThe LCM of ", a, " and ", w, " is ", lcm(a,w), "\n")