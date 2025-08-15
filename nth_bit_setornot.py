def setOrNot(number, n):
    mask = 1
    if (n & mask) == 1 or (n & mask) == 0:
        if number & (1 << n):
            print("SET")
        else:
            print("NOT SET")
number = int(input("Enter the number: "))
n = int(input("Enter the bit position (0-indexed): "))
setOrNot(number, n)