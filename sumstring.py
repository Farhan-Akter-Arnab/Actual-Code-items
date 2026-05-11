# A sum-string is a number where each digit (starting from the third) is the sum of the previous two digits.
def Issumstring(n):
    numlist = list(str(n))
    
    # Base case: if 2 or fewer digits, it's a valid sum-string
    if len(numlist) <= 2:
        return True
    
    # Check if the last digit equals sum of previous two digits
    if int(numlist[-3]) + int(numlist[-2]) != int(numlist[-1]):
        return False
    
    # Remove the last digit and recursively check the remaining number
    prefix = numlist[:-1]
    new_num = int(''.join(prefix))
    return Issumstring(new_num)

# Driver code
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if Issumstring(number):
        print(f"{number} is a sumstring.")
    else:
        print(f"{number} is not a sumstring.")