num = int(input("Enter any positive integer [natural number]: "))
print("The numbers upto your input n with power 1 are: ")
for i in range(1, num+1):
    print(i)
print("The numbers upto your input n with power 2 are: ")
for i in range(1, num+1):
    print(i**2)
print("The numbers upto your input n with power 3 are: ")
for i in range(1, num+1):
    print(i**3)
print("The numbers upto your input n with power respective to their order are: ")
for i in range(1, num+1):
    print(i**i)
print("The numbers upto your input n with values of n raised to the power of [n+1] are: ")
for i in range(1, num+1):
    print(i**(i+1))
print("The numbers upto your input n with values of [n+1] multiplied with n raised to the power of [n+1] are: ")
for i in range(1, num+1):
    print(((i+1)*i**(i+1)))