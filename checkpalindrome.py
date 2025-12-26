# function to reverse the string
def reverse(s):
    n = len(s)
    # converting string to list
    li = list(s)
    for i in range(n//2):
        # swapping the characters
        li[i], li[n-i-1] = li[n-i-1], li[i]
    return "".join(li)
# function to check if the string is palindrome
def checkPalindrome(s):
    # ignoring case
    s = s.lower()
    rev_string = reverse(s)
    if s == rev_string:
        return True
    else:
        return False
# Driver code
inp = input("Enter a string: ")
if checkPalindrome(inp):
    print(inp, "is a palindrome!")
else:
    print(inp, "is not a palindrome...")