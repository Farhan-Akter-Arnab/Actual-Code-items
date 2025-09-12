def take_input():
    num = int(input("Enter a number: "))
    if num < 0 or type(num) != int:
        print("Invalid value entered, stopping.")
        return
    else:
        print("You entered:", num)
        take_input()
        
take_input()