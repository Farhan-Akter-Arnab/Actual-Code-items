# Function to sort a string of lowercase letters in alphabetical order

def sort(s):
    # Code here
    li = []
    ans = ""
    for i in range(26):
        li.append(0)
    for i in range(len(s)):
        ind = ord(s[i]) - ord('a')
        li[ind] += 1
    for i in range(26):
        if li[i] >= 1:
            for j in range(li[i]):
                ans = ans + chr(i + ord('a'))
        else:
            continue
    return ans

# Example usage:
if __name__ == "__main__":
    input_str = input("Enter a string of lowercase letters: ").lower()
    sorted_str = sort(input_str)
    print("Sorted string:", sorted_str)