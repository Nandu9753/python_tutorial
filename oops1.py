class Vehicle:
    def __init__(self) -> None:
        pass
       #  self.name = name
        # self.brand = brand
    def set(self,name,brand):
        self.name = name    
        self.brand = brand
    def show(self):
        print("Vehicle Name:",self.name)
        print("Brand Name:",self.brand)
v= Vehicle()
v.set("Bus","mahindra")
v.show()            