class Car:
    def __init__(self, brand, model): #__init__ called constructor
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Car Brand : {self.brand}, Car model : {self.model}"


myCar = Car("Toyota", "2026")
print(myCar.fullName())

class ElectricCar(Car):
    def __init__(self, brand, model, battery): 
        super().__init__(brand, model) #super() is used to call the constructor of the parent class
        self.battery = battery 

    def fullName(self):
        return f"Car Brand : {self.brand}, Car model : {self.model}, Battery : {self.battery}" 

myElectricCar = ElectricCar("Tesla", "Model S", "100 kWh")
print(myElectricCar.fullName())  
print(myElectricCar.battery)  