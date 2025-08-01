n = int(input("Enter a number: "))
result = 0
temp = n
while temp != 0:
    digit = temp % 10
    result = result + digit ** len(str(n))
    temp = temp // 10
print(result)
if n == result:
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")