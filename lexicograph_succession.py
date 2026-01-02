def nextWord(s):
    # If the string is empty, return "a"
    if (s.split() == ""):
        return "a"
    
    # Find the first character from the right
    # which is not z
    i = len(s) - 1
    while (s[i] == 'z' and i>=0):
        i -= 1
    
    # If all characters are z, then we need to
    # add an extra character 'a' at the end
    if (i == -1):
        s = s + 'a'
    # If there are some non-z characters
    else:
        s = s.replace(s[i], chr(ord(s[i]) + 1), 1)
    
    return s

# Driver code
inp = input("Enter a word: ")
print("Next word is:", nextWord(inp))