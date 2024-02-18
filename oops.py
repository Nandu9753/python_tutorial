# Define a class called 'Car'
class Car:
    # Class constructor (initialization method)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Method to start the car
    def start(self):
        print(f"{self.year} {self.make} {self.model} is starting.")

    # Method to accelerate the car
    def accelerate(self, increment):
        self.speed += increment
        print(f"The car is now moving at {self.speed} mph.")

    # Method to brake the car
    def brake(self, decrement):
        self.speed -= decrement
        print(f"The car is slowing down to {self.speed} mph.")

    # Method to stop the car
    def stop(self):
        self.speed = 0
        print(f"{self.year} {self.make} {self.model} has stopped.")

# Create an instance (object) of the 'Car' class
my_car = Car("Toyota", "Camry", 2020)

# Access and modify attributes
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")
my_car.start()
my_car.accelerate(30)
my_car.brake(10)
my_car.stop()
