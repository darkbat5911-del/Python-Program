class Car:
    def __init__(self, brand, model): #__init__ called constructor
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Car Brand : {self.brand}, Car model : {self.model}"


myCar = Car("Toyota", "2026")
print(myCar.fullName())



# print(myCar.brand, myCar.model)
# myNewCar = Car("Innova" , "2028")
# print(myNewCar.model)
# Car brand : Toyota , Car Model :