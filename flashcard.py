class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        # we will return a string
        return self.word + " : " + self.meaning
flash = []

print("Welcome to Flashcard Application")
# the following steps will be repeated until
# the user chooses to stop adding the flashcards
while True:
    word = input("Enter the word which you want to add: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    option = int(input("If you want to add more flashcards, press 0, otherwise enter 1: "))
    if option:
        break
    
#printing all the flashcards
print("\n Your flashcards are: ")
for i in flash:
    print(">", i)