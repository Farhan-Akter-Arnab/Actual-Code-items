# function to count the number of words in a given string
def wordcount(s):
    count = 0
    # removing leading and trailing spaces from string
    s = s.strip()
    for i in range(len(s)):
        # checking for spaces in the string
        if s[i] == ' ':
            count += 1
    return count + 1 # adding 1 to count for the last word
def word_compare(s1,s2):
    w_count1 = wordcount(s1)
    w_count2 = wordcount(s2)
    if w_count1 > w_count2:
        return f"The first string has more words: {w_count1} words."
    elif w_count2 > w_count1:
        return f"The second string has more words: {w_count2} words."
    else:
        return f"Both strings have the same number of words: {w_count1} words."
# driver code
str1 = input("Enter the first string (sentence): ")
str2 = input("Enter the second string (sentence): ")
print("Number of words in the first string:", wordcount(str1), " and in the second string:", wordcount(str2))
print(word_compare(str1, str2))