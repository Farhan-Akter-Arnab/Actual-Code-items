# take marks as input from user
print("Enter Marks Obtained in several subjects: ")
Religion = float(input("Religion : "))
Mathematics = float(input("Mathematics : "))
Physics = float(input("Physics : "))
Chemistry = float(input("Chemistry : "))
Biology = float(input("Biology : "))
Technology = float(input("ICT : "))
History = float(input("BGS : "))
English = float(input("English : "))
Bangla = float(input("Bangla : "))

# Let's calculate the percentage of marks
sum = Religion+Mathematics+Physics+Chemistry+Biology+Technology+History+English+Bangla
print("sum of all the given subjects")
perc = (sum/900)*100
print("Percentage Mark = ", perc, " %")