from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Fish(Animal):
    def move(self):
        print("I can swim")
class Duck(Animal):
    def move(self):
        print("I can swim and fly")
class Snail(Animal):
    def move(self):
        print("I can crawl")
H = Human()
H.move()
F = Fish()
F.move()
D = Duck()
D.move()
S = Snail()
S.move()