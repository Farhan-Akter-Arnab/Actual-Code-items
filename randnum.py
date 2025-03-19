import random
playing = True
number = str(random.randint(8,24))
print("I will generate a number from 8 to 24, and you have to guess the number one num at a time.")
print("The game ends when you get one right!")
while playing:
    guess = input("Give me your best guess! ")
    if number == guess:
        print("You win the game!")
        print("The number was ", number)
        break
    else:
        print("Your guess is not quite right, try again.")