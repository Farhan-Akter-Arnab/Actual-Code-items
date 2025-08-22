def power2(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

n = int(input("Enter a number: "))
if power2(n):
    print("\nThe number, ", n, " is a power of 2.")
else:
    print("\nThe number, ", n, " is not a power of 2.")