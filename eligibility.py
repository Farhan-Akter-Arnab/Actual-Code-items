medical_cause = input("Did you have a medical cause? Type Yes or No: ")
#Take input of the attendance
attendance = int(input("Enter the attendance of the student: "))
if medical_cause == 'Yes': #checking the condition 1
    print("You are allowed")
else:
    if attendance >= 80: #checking the condition 2
        print("You are allowed")
    else:
        print("You are NOT ALLOWED")