def palind(r):
    e = len(r) - 1
    s = 0
    while (s < e):
        if (r[s] != r[e]):
            return False
        s += 1
        e -= 1
    return True
r = (1, 2, 3, 3, 2, 1)
if (palind(r)):
    print("The Tuple is Palindrome")
else:
    print("The Tuple is not Palindrome")
r = (2, 4, 6, 8, 10, 8, 6, 4, 2)
if (palind(r)):
    print("The Tuple is Palindrome")
else:
    print("The Tuple is not Palindrome")
r = ('o', 'g', 'h', 'u', 'z')
if (palind(r)):
    print("The Tuple is Palindrome")
else:
    print("The Tuple is not Palindrome")