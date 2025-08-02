m = int(input("Please enter the first number: "))
n = int(input("Please enter the second number: "))
def lcm (m,n):
    greater = max(m,n)
    while True:
        if greater % m == 0 and greater % n == 0:
            return greater
        greater += 1

print(lcm(m, n))