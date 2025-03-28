numlimit = int(input("Enter the number upto which you want to print odd numbers: "))
numlist = [x for x in range(0,(numlimit+1)) if x%2 != 0]
print("The list of odd numbers upto your given value: ")
print(numlist)
fruits = ["dates", "grape", "fig", "watermelon", "pommegranate", "olive"]
fruitlist = [x.capitalize() for x in fruits]
print("List of fruits: ")
print(fruitlist)