# Function for determining the number of occurrences of each character in a string
def frequency(s):
    s = s.lower()
    d = {}
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d
# Function to find the first non-repeating character in a string
def nonrep_char(s):
    freq = frequency(s)
    for char in s:
        if freq[char.lower()] == 1:
            return char
    return None
# Driver code
inp = input("\nEnter a string: ")
result = nonrep_char(inp)
if result:
    print("The first non-repeating character is:", result, "\n")
else:
    print("There are no non-repeating characters.\n")