def reversebits(n):
    result = 0
    while n > 0:
        result <<= 1
        print("Current result = ", result)
        result |= n & 1
        print("Current result after OR = ", result)
        n >>= 1
        print("Current n after shift = ", n)
    return result
n = int(input("Enter a number to reverse its bits: "))
print("Reversed bits: ", reversebits(n))