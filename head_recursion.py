def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

n = int(input("Enter the upper limit of numbers: "))
print_numbers(n)