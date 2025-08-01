def bin_to_dec(n):
    num = 0
    temp = n
    while temp != 0:
        for i in range(0, len(str(temp))):
            num += (temp % 10) * (2 ** i)
            temp //= 10
    return num
nn = int(input("Enter a binary number: "))
print("The decimal format of ", nn, " is ", bin_to_dec(nn))