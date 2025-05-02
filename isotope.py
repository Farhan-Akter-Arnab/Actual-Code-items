# Class
class Tritium():
    def Z(self):
        print("Atomic Number of Tritium = ", 1)
    def A(self):
        print("Mass Number of Tritium = ", 3)
    def use(self):
        print("Tritium is used in radioluminescence, nuclear plants and bombs.\n")
# Class
class Carbon14():
    def Z(self):
        print("Atomic Number of Carbon-14 = ", 6)
    def A(self):
        print("Mass Number of Carbon-14 = ", 14)
    def use(self):
        print("Carbon-14 is used mainly to determine the age of fossils.")
# Object Creation
obj_3H = Tritium()
object_14C = Carbon14()
# Common Interface
for isotope in (obj_3H, object_14C):
    isotope.Z()
    isotope.A()
    isotope.use()