bill = float(input("Enter your bill amount: "))
tip = float(input("Enter the percentage of your tip in numbers; {write 5 in case of 5%} : "))
def total_calc(bill_amount, tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print("Please pay ", total)
total_calc(bill, tip)