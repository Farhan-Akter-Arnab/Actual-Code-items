num = int(input("Enter any number to convert from decimal to binary: "))
binary_num = ""
while num > 0:
    binary_num = str(num % 2) + binary_num
    num = num // 2
print("The required number in binary format is: ", int(binary_num))