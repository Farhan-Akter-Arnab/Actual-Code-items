num = int(input("Enter any number: "))
sum = 0
# find the sum of the power of value of number of digits of each digit
temp = num
c = str(temp)
n = len(c)
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
if num == sum:
    print(num, " is an Armstrong number")
else:
    print(num, " is not an Armstrong number")