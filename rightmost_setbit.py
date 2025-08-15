def rightmost_set_bit(n):
    if n == 0:
        return None
    return n & -n
n = int(input("Enter a number: "))
result = rightmost_set_bit(n)
if result is None:
    print("The number is zero, no set bits.")
else:
    print("The rightmost set bit is:", result)