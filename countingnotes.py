# Taking total amount as input from user
Amount = int(input("Please enter amount for withdraw : "))
# Calculating the number of notes of different denominations
note_1 = Amount//1000
note_2 = (Amount%1000)//500
note_3 = ((Amount%1000)%500)//100
note_4 = (((Amount%1000)%500)%100)//50
note_5 = ((((Amount%1000)%500)%100)%50)//20
note_6 = (((((Amount%1000)%500)%100)%50)%20)//10

print("notes of 1000 Taka : ", note_1)
print("notes of 500 Taka : ", note_2)
print("notes of 100 Taka : ", note_3)
print("notes of 50 Taka : ", note_4)
print("notes of 20 Taka : ", note_5)
print("notes of 10 Taka : ", note_6)