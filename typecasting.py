name = "Hans ∅rsted"
age = 73
is_student = False
weight = 55.55

print("Name : ", name)
print("Data Type of Name is ", type(name))
print("Age : ", age)
print("Data Type of Age is ", type(age))
print("Is he a student? ", is_student)
print("Data Type of 'Is he a student?' is ", type(is_student))
print("Weight : ", weight)
print("Data Type of Weight is ", type(weight))

print("\n After Type Casting...")
age = str(age)
print(age)
print("Data type of age is ", type(age))
weight = int(weight)
print(weight)
print("Data type of weight is ", type(weight))