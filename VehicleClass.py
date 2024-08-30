class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Info: {self.make} {self.year} {self.model}")

    def start(self):
        print('Is starting')

#Inheritance

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        print(f"Bike Info: {self.year} {self.make} {self.model}, {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, typeofbike):
        super().__init__(make, model,year)
        self.typeofbike = typeofbike

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}, {self.typeofbike}")

if __name__ == "__main__":
    vehicle = Vehicle("Generic", "Model", 2002)
    car = Car("Toyato","Camry", 2022, 4)
    motorcycle = Motorcycle("Honda", "Sportster", 2021, "Cruiser")

    vehicle.display_info()
    vehicle.start()
    car.display_info()
    motorcycle.display_info()
    motorcycle.start()
