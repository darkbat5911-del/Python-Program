class Car:

    totalCars = 0
    def __init__(self, brand, model): #__init__ called constructor
        self.__brand = brand
        self.model = model
        Car.totalCars += 1


    def get_Brand(self):
        return self.__brand + " !"

    def fullName(self):
        return f"Car Brand : {self.__brand}, Car model : {self.model}"

    def fuelType(self):
        return "Petrol or Diesel"

    @staticmethod
    def generalDescription(): 
        return "This is a car with a petrol or diesel engine"


myCar = Car("Toyota", "2026")
# print(myCar.fullName())

class ElectricCar(Car):
    def __init__(self, brand, model, battery): 
        super().__init__(brand, model) #super() is used to call the constructor of the parent class
        self.battery = battery 

    def fullName(self):
        return f"Car Brand : {self.brand}, Car model : {self.model}, Battery : {self.battery}" 

    def fuelType(self):
        return "Electric charge"

    @staticmethod #Decorator to make the method static
    def generalDescription():
        return "This is a car with an electric engine"

myElectricCar = ElectricCar("Tesla", "Model S", "100 kWh")
print(ElectricCar.generalDescription())
print(Car.generalDescription())
myCar = Car("Toyota", "2026")
