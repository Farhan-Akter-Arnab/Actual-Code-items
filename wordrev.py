def reverse_words(s):
    elements = s.split()
    revelements = elements[::-1]
    reversed_string = ' '.join(revelements)
    print("The reversed form of the string: ",reversed_string)
string = input("Enter a string: ")
reverse_words(string)