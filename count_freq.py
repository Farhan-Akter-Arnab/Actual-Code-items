# Counting the frequency of characters in a given string
# By creating dictionary

def frequency(s):
    # creating a dictionary to store frequency
    # of each character
    s = s.lower()
    d = {}
    
    for i in range(len(s)):
        # checking if the character is already
        # in dictionary
        if s[i] in d.keys():
            # incrementing the count of character
            d[s[i]] += 1
        else:
            # initializing the count of character
            d[s[i]] = 1
            
    return d

# Driver code
inp = input("Enter a string: ")
print(frequency(inp))