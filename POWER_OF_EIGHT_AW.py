def POWER_OF_EIGHT(a):
    exponent = 0
    if a <= 0:
        return False
    while a % 8 == 0:
        exponent += 1
        a //= 8
    print("Floor of Exponent:", exponent)
    return exponent > 0 and a == 1
w = int(input("Enter a number: "))
if POWER_OF_EIGHT(w):
    print("The number ", w, " is a power of 8")
else:
    print("The number ", w, " is not a power of 8")