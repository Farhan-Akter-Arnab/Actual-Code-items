def Print(n):
    if n == 0:
        return
    print("Printed value is = ", n)
    Print(n - 1)

A = int(input("Enter how many times do you want this to be printed: "))
Print(A)