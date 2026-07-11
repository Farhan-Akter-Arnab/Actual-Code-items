def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[n]
# Example usage:
string = "mathematics"
dictionary = ["math", "mat", "at", "hat", "he", "ic", "cs", "ics", "them", "mathematics"]
if word_break(string, dictionary):
    print(f"The string '{string}' can be segmented into words from the dictionary.")
else:
    print(f"The string '{string}' cannot be segmented into words from the dictionary.")