# This function removes extra spaces from a given string.

def removespaces(s):
    result = ""
    n = len(s)
    
    # Iterate through each character in the string
    for i in range(n):
        if s[i] == ' ':
            if i > 0 and i < n - 1:
                result += ''
        else:
            result += s[i]
    
    # If the result is alphanumeric, remove all spaces
    if result.isalnum():
        result = ''.join(result.split())
    return result

# Example usage:
inp = input("Enter a string: ")
out = removespaces(inp)
print("String after removing extra spaces:")
print(out)