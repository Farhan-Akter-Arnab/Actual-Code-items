class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 24)
print("Blu is a ", blu.species)
print("Woo is a ", woo.species)
print(blu.name, " is ", blu.age, " years old")
print(woo.name, " is ", woo.age, " years old")