# Function to remove vowels from a given string

def removevowels(s):
    s.lower()
    result = ""
    
    # list containing vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(s)):
        # checking the presence of vowels in the string
        
        if s[i] in vowels:
            # removing vowels
            result = result + ""
        else:
            result = result + s[i]
    
    return result

# Driver code
if __name__ == "__main__":
    inp = input("Enter a string: ")
    print("String after removing vowels: ", removevowels(inp))