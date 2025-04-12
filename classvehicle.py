class Vehicle:
    def __init__(self, max_speed, mileage):
        # bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
print("Model Max Speed: ", modelX.max_speed)
print("Model Mileage: ", modelX.mileage)