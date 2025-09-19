def reversenumber(num):
    if (num > 0):
        last = num % 10
        if (num // 10 > 0):
            current_number = reversenumber((int)(num // 10))
            return last*pow(10, len(str(current_number))) + current_number
        return num

n = int(input("Enter your number: "))
print("Reversed Number: ", reversenumber(n))