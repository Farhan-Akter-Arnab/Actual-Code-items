n = int(input("Enter your number: "))
def checkifpower(n):
    if (n <= 0):
        return False
    if (n == 1):
        return True
    if (n % 2 == 0):
        return checkifpower(n / 2)
    return False

if (checkifpower(n)):
    print(n, "is a power of 4")
else:
    print(n, "is not a power of 4")