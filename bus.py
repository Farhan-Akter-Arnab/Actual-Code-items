class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass

School_Bus = Bus("School Mathematics", 180, 24)
print("Vehicle Name:", School_Bus.name, "Maximum Velocity:", School_Bus.max_speed, "Mileage:", School_Bus.mileage)