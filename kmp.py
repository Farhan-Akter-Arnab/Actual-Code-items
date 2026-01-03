def KMPpattern(pat, txt):
    M, N, lps, j = len(pat), len(txt), [0]*len(pat), 0
    LPSArray(pat, M, lps)
    i = 0
    while (N-i) >= (M-j):
        if pat[j] == txt[i]:
            i += 1; j += 1
        if j == M:
            print("Found pattern at index " + str(i-j)); j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0: j = lps[j-1]
            else: i += 1
def LPSArray(pat, M, lps):
    length, i = 0, 1
    lps[0]
    while i < M:
        if pat[i] == pat[length]:
            length += 1; lps[i] = length; i += 1
        else:
            if length != 0: length = lps[length-1]
            else: lps[i] = 0; i += 1
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")
KMPpattern(pattern, text)            