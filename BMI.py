h = float(input("Enter your height in centimetres: "))
m = float(input("Enter your mass in kilograms: "))
BMI = m/(h/100)**2
print("Your BMI [Body Mass Index] is: ", BMI)
if BMI <= 18.4:
    print("You are underweight. Please take more nutritious food!")
elif BMI <= 24.9:
    print("You are healthy. There is almost no problem for this.")
elif BMI <= 29.9:
    print("You are overweight. Please take care of the amount you eat!")
elif BMI <= 34.9:
    print("You are severely overweight. Abstain from taking excess carbohydrates, fat and sugar.")
elif BMI <= 39.9:
    print("You are obese. Please exercise regularly and abstain from excess fat, sugar, salt, carbs etc.")
else:
    print("YOU ARE SEVERELY OBESE!!! DO EXERCISE REGULARLY, AVOID ANY SUGAR, FAT, OR EXCESS CARBOHYDRATES; AND FAST AT LEAST THREE DAYS A MONTH!!!")