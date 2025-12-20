# function to reverse the string

def reverse(s):
    # length of string
    n = len(s)
    # converting string to list
    li = list(s)
    
    # traversing half of the string
    
    for i in range(n//2):
        
        # swapping first and last, second and second last, and so on.
        li[i], li[n-i-1] = li[n-i-1], li[i]
        
    return "".join(li)

# driver code

if __name__ == "__main__":
    # taking input from user
    inp = input("Enter a string: ")
    print("Original String:", inp)
    print("Reversed String:", reverse(inp))