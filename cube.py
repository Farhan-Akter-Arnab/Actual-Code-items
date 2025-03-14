def square(num):
    return num * num
def extra(n,t):
    return n * t

n1 = float(input("Enter any number: "))
print("The cube of your number is: ", extra(square(n1),n1))