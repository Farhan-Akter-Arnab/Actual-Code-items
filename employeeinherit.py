class Person(object):
    def __init__(self, name, userid):
        self.name = name
        self.userid = userid
    def display(self):
        print("Name: ", self.name)
        print("User ID: ", self.userid)
class Employee( Person ):
    def __init__(self, name, userid, salary, post):
        self.salary = salary
        self.post = post
        # invoking the __init__ of the parent class
        Person.__init__(self, name, userid)
# creation of an object variable or an instance
a = Employee("Oghuz Khan", 314159, 2940000, "Manager")
a.display()