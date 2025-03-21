def match_words(words):
    ctr = 0
    list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            list.append(word)
    print("List of words with first and last character same:\n",list)
    return ctr
count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221', '8248'])
print("Number of words having first and last character same: ", count)