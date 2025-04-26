try:
    class myClass:
        __privateVar = 24
        def __privMeth(self):
            print("I am inside a private method")
        def hello(self):
            print("Private variable value: ", myClass.__privateVar)
    foo = myClass()
    foo.hello()
    foo.__privMeth()
except AttributeError as ex:
    print("Error has been taken place: ", ex)