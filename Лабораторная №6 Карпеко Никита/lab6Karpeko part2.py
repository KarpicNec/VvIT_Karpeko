class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"Это транспортное средство: {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        vehic_info = super().get_info()
        return f"{vehic_info}, тип топлива: {self.fuel_type}"

vehicle = Vehicle("Hyundai", "Solaris")
print(vehicle.get_info())

car1 = Car("Tesla", "IDK_Mask", "электричество")
print(car1.get_info())

car2 = Car("Lada", "Granta", "бензин")
print(car2.get_info())
    
