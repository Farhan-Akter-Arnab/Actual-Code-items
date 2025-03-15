var = int(input("Enter any integer value greater than 0: "))
print('\nCurrent variable value : ', var)
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('\nCurrent variable value : ', var)
print("\nGood bye!")