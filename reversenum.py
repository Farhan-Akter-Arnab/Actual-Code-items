number = int(input("Enter a number: "))
print("Numbers in ascending order: \n")
for i in range(1, number+1):
    print(i)
print("\nNumbers in descending order: \n")
for i in range(number, 0, -1):
    print(i)