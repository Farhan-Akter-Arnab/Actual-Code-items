# Dividing two integers without using multiplication, division and mod operator.

def divide(ourdividend, ourDivisor):
    sign = (-1 if((ourdividend < 0) ^ (ourDivisor < 0)) else 1)
    ourdividend = abs(ourdividend)
    ourDivisor = abs(ourDivisor)
    
    quotient = 0
    tempNumber = 0
    for i in range(31, -1, -1):
        if (tempNumber + (ourDivisor << i) <= ourdividend):
            tempNumber += ourDivisor << i
            quotient |= 1 << i
    if sign == -1:
        quotient = -quotient
        
    return quotient
    
a = int(input("Enter the value of a for a/b: "))
b = int(input("Enter the value of b for a/b: "))
print("Result of ", a, " / ", b, " is: ", divide(a, b))

if __name__ == "__main__":
    divide(a, b)