import random
options = ["rock", "paper", "scissors"]
user_choice = input("Choose rock, paper or scissors: ").lower()
computer_choice = random.choice(options)
print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("Rock smashes Scissors! You have won!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("Paper covers Rock! You have won!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("Scissors cut Paper! You have won!")
else:
    print("You have lost!")