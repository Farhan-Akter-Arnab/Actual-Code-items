def sum_upto(n):
    if n <= 1:
        return n
    else:
        return n + sum_upto(n - 1)
num = int(input("Enter a positive integer to sum up to 1 from your number: "))
result = sum_upto(num)
print("The sum of integers from 1 to ", num, " is = ", result)