def longest_consecutive_ones(n):
    binary = bin(n)[2:]
    print("Binary representation of ", n, " = ", binary)
    longest = max(map(len, binary.split('0')))
    return longest
number = int(input("Enter a number: "))
result = longest_consecutive_ones(number)
print("Longest consecutive 1s in binary representation of", number, "is", result)