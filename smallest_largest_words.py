# Program to find out the smallest and largest word in a string
def smallest_largest_words(str1):
    word = ""
    all_words = []
    str1 = str1 + " "
    for i in range(0, len(str1)):
        if (str1[i] != " "):
            word = word + str1[i]
        else:
            all_words.append(word)
            word = ""
    small = large = all_words[0]
# Finding smallest and largest word in the list of words in str1    
    for k in range(0, len(all_words)):
        if (len(small) > len(all_words[k])):
            small = all_words[k]
        if (len(large) < len(all_words[k])):
            large = all_words[k]
    return small, large
str1 = input("Enter a string consisting of one or more sentences: ")
print("Original strings:\n", str1)
small, large = smallest_largest_words(str1)
print("Smallest word: ", small)
print("Largest word: ", large)