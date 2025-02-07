cost = float(input("Enter the cost price of your item: "))
sell = float(input("Enter the selling price of your item: "))
print("Your cost price is ", cost, " Taka; and your selling price is ", sell, " Taka.")
if sell > cost:
    profit = (sell - cost)
    perprof = (profit / cost) * 100
    print("Your profit is ", profit, " Taka. And the percentage is ", perprof, "%")
elif cost > sell:
    loss = (cost - sell)
    perloss = (loss / cost) * 100
    print("Your profit is ", loss, " Taka. And the percentage is ", perloss, "%")
else:
    print("There is neither profit nor loss in your amount.")