# This program checks if one string is a substring of another and...
# returns the index of its first occurrence.

def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    
    return -1

# Example usage:


if __name__ == "__main__":
    
    s1 = input("Enter the substring to search for: ")
    s2 = input("Enter the string to search within: ")
    
    result = isSubstring(s1, s2)
    
    if result == -1:
        print("Substring not found.")
    
    else:
        print("Substring found at index: ", str(result))