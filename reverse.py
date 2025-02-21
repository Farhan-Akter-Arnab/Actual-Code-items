num = int(input("Enter a number: "))
temp = num
c = str(temp)
n_digits = len(c)
numstr = ('')
numrev = 0
print("The number of digits of your number is = ", n_digits)
numstr = c[::-1]
numrev = int(numstr)
print('The reversed form of your number is ', numrev)
if num == numrev:
    print("Your number is a palindromic number!!!")