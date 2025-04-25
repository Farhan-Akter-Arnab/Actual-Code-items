class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
# child class
class Chicken(Bird):
    def __init__(self):
        super().__init__()
        print("Chicken is ready")
    def whoisThis(self):
        print("Chicken")
    def run(self):
        print("Run faster")
bird = Chicken()
bird.whoisThis()
bird.swim()
bird.run()