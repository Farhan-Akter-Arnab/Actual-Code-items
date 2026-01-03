def searchPattern(pattern, text, q):
    m, n= len(pattern), len(text)
    d = len(set(text))
    p, t, h, i, j = 0, 0, 1, 0, 0
    for i in range(m-1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("Pattern is found at position: " + str(i+1))
        if i < n-m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0:
                t = t + q
text = input("Please enter the text: ")
pattern = input("Enter which characters or strings you want to find: "); q = len(text) + len(pattern)
searchPattern(pattern, text, q)