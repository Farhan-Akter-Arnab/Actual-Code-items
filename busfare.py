class Vehicle:
    def __init__(self, name, velocity):
        self.name = name
        self.velocity = velocity
class Bus(Vehicle):
    def __init__(self, name, velocity, fare, passengers):
        super().__init__(name, velocity)
        self.fare = fare
        self.passengers = passengers
    def calculate_fare(self):
        return self.fare * self.passengers
bus = Bus("Mathematical Bus", 240, 10, 80)
print("There were ", bus.passengers, "passengers on the bus named ", bus.name, ", whose velocity was ", bus.velocity, " m/s.")
print("The total fare collected from the passengers must be ", bus.calculate_fare(), " Dinars.")