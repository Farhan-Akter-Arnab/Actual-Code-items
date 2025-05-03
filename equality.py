# Python program to overload equality
# and less than operators
class A :
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if (self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if (self.a == other.a):
            return "ob1 is equal to ob2"
        else:
            return "ob1 is not equal to ob2"
        
ob1 = A(8)
ob2 = A(24)
print("Passed values are: ", ob1.a, ",", ob2.a)
print(ob1 < ob2)
ob3 = A(2**3)
ob4 = A(4**(3/2))
print("Passed values are: ", ob3.a, "," , ob4.a)
print(ob3 == ob4)