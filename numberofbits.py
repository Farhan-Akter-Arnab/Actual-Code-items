def number_of_bits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count
n = int(input("Enter a number: "))
print("Number of bits in the number", n, "is", number_of_bits(n))