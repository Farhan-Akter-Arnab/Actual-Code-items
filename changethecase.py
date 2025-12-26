# Python3 code to demonstrate the
# changing lower case to upper case
# and vice versa of string characters

def changeTheCase(s):
    result = ""
    
    for i in s:
        
        # changing lower case to upper case
        if i.islower():
            result = result + i.upper()
        
        # changing upper case to lower case
        if i.isupper():
            result = result + i.lower()
    
    return result

# Driver code

inp = input("Enter the string: ")
print("String after changing lower case to upper case and vice versa : - ")
print(changeTheCase(inp))