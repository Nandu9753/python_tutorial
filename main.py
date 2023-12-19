class Vehicle:
    def __init__(self,name,brand) -> None:
        self.name = name
        self.brand = brand
    def set_vehicle(self,name,brand):
        print("Set before")
        print("Vehicle Name:",self.name)    
        print("Brand Name:",self.brand)
        self.name = name
        self.brand = brand
    def get_vehicle(self):  
        print("Vehicle Name:",self.name)    
        print("Brand Name:",self.brand)
v = Vehicle("Bike","Hf")
v.set_vehicle("Car","tata")
v.get_vehicle()