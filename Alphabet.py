anything = input("Enter any item or thing: ")
if anything >= 'A' and anything <= 'Z':
    print("It is a capital letter!")
elif anything >= 'a' and anything <= 'z':
    print("It is a small letter!")
else:
    print("It is not included in the English Alphabet")