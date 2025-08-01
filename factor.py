# Function to print the factors of a number
def print_factors(n):
    print("The factors of ", n, " are: ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
num = int(input("Enter your number to find its factors: "))
print_factors(num)