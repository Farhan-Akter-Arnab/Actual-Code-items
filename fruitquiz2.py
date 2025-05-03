import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {'dates': 'brown',
                       'grapes': 'green',
                       'olive': 'green',
                       'fig': 'purple',
                       'orange': 'orange',
                       'pommegranate': 'red'}
    def ghora(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of ", fruit)
            user_answer = input().lower()
            if (user_answer == color):
                print("Correct answer")
            else:
                print("Wrong answer")
            option = int(input("Do you want to continue? 1 for yes, 0 for no:"))
            if option == 0:
                break
print("Welcome to fruit quiz")
fq = FruitQuiz()
fq.ghora()