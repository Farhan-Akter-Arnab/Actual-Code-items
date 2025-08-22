def isPowerOfFour(a):
    if a <= 0:
        return False
    while a % 4 == 0:
        a //= 4
    return a == 1

n = int(input("Enter a number: "))
if isPowerOfFour(n):
    print("\nThe number ", n, " is a power of 4.")
else:
    print("\nThe number ", n, " is not a power of 4.")