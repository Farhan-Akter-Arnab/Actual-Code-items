num = float(input("Enter any number: "))
if ((num*10)%10)!=0:
    print("Your number ", num, " is a real number, but not an integer")
    Re = num
    if Re<0:
        print("Your number ", Re, " is a negative, non-integer number")
    elif Re>0:
        print("Your number ", Re, " is positive but not natural")
    else:
        print("Your number is [0]")
elif ((num*10)%10)==0:
    print("Your number ", num, " is a real number and an integer")
    n = num
    if n<0:
        print("Your number ", n, " is a negative number")
        if n%10==1:
            print("The last digit of your integer is 9")
        elif n%10==2:
            print("The last digit of your integer is 8")
        elif n%10==3:
            print("The last digit of your integer is 7")
        elif n%10==4:
            print("The last digit of your integer is 6")
        elif n%10==5:
            print("The last digit of your integer is 5")
        elif n%10==6:
            print("The last digit of your integer is 4")
        elif n%10==7:
            print("The last digit of your integer is 3")
        elif n%10==8:
            print("The last digit of your integer is 2")
        elif n%10==9:
            print("The last digit of your integer is 1")
        else:
            print("The last digit of your integer is 0, divisible by 10.")
    elif n>0:
        print("Your number ", n, " is a natural number")
        if n%10==1:
            print("The last digit of your integer is 1")
        elif n%10==2:
            print("The last digit of your integer is 2")
        elif n%10==3:
            print("The last digit of your integer is 3")
        elif n%10==4:
            print("The last digit of your integer is 4")
        elif n%10==5:
            print("The last digit of your integer is 5")
        elif n%10==6:
            print("The last digit of your integer is 6")
        elif n%10==7:
            print("The last digit of your integer is 7")
        elif n%10==8:
            print("The last digit of your integer is 8")
        elif n%10==9:
            print("The last digit of your integer is 9")
        else:
            print("The last digit of your integer is 0, divisible by 10.")
    else:
        print("Your number is a [0]")
    