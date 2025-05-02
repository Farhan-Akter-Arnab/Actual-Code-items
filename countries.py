# Class 1
class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")
    def language(self):
        print("Bangla is the predominant language of Bangladesh.")
    def type(self):
        print("Bangladesh is a developing country.")
# Class 2
class Russia():
    def capital(self):
        print("Moscow is the capital of Russia.")
    def language(self):
        print("Russian is the predominant language of Russia.")
    def type(self):
        print("Russia is a developed country.")
# Object Creation
obj_bd = Bangladesh()
obj_rus = Russia()
# Common Interface
for country in (obj_bd, obj_rus):
    country.capital()
    country.language()
    country.type()