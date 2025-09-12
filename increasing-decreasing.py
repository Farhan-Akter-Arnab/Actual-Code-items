def incdec(n, num):
    if (n < 1 or n > num):
        return
    print(n, end='\n')
    incdec(n - 1, num)
    print(n, end='\n')
num = int(input("Enter a positive integer n : "))
incdec(num, num)