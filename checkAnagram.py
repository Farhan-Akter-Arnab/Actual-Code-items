def frequency(s):
    s = s.lower()
    d = {}
    for i in range(len(s)):
        # checking if the character is already in the dictionary
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d
def checkAnagrams(s1, s2):
    d_s1 = frequency(s1)
    d_s2 = frequency(s2)
    if d_s1 == d_s2:
        return True
    else:
        return False
# Driver code
inp1 = input("Enter first string: ")
inp2 = input("Enter second string: ")
if checkAnagrams(inp1, inp2):
    print("The strings are anagrams!")
else:
    print("The strings are not anagrams...")