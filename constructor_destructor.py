# Create class
class Employee:
    # Initializing
    def __init__(self):
        print("Employee created")
    # Calling DESTRUCTOR
    def __del__(self):
        print("Destructor called")
def Create_Obj():
    print("Making object...")
    obj = Employee()
    print("Function is ended")
    return obj
print('Calling Create_Obj() function')
obj = Create_Obj()
print("Program has been ended")