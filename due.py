bill = float(input("Enter the amount of bill to be paid: "))
pay = float(input("Enter the amount you want to pay on every investment or turns: "))
remain = bill - pay
while remain > 0:
    remain = remain - pay
    print("You will have to pay more = ", remain)
    if remain <= 0:
        break