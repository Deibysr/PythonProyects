"""
Responsabilidad Única: Car y Motorcycle se encargan de implementar los detalles específicos de cada tipo de vehículo.
Abierto/Cerrado: VehicleSOLID actúa como una abstracción para vehículos, permitiendo que el sistema se extienda (con nuevas clases para diferentes tipos de vehículos) sin modificar el código existente.
Sustitución de Liskov: Las clases derivadas (Car, Motorcycle) pueden ser utilizadas en lugar de su clase base (VehicleSOLID) sin afectar la correctitud del programa.
Segregación de Interfaces: Cada clase implementa solo los métodos que necesita (por ejemplo, ride para Motorcycle y drive para Car), aunque este ejemplo es bastante simplificado y no muestra interfaces explícitas, el diseño apunta hacia este principio al separar los comportamientos.
Inversión de Dependencias: Aunque este ejemplo es simple y no demuestra completamente el principio, la estructura está preparada para depender de abstracciones (como sería una interfaz de vehículo) en lugar de detalles concretos.
"""

# Ejemplo que no sigue los principios SOLID

class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
    
    def get_price(self):
        if self.type == "car":
            return f"The price for the car {self.model} is {self.price}"
        elif self.type == "motorcycle":
            return f"The price for the motorcycle {self.model} is {self.price}"
    
    def drive(self):
        if self.type == "car":
            return "Driving a car"
        elif self.type == "motorcycle":
            return "Riding a motorcycle"

# Ejemplo que sigue los principios SOLID

class VehicleSOLID:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_price(self):
        pass

class Car(VehicleSOLID):
    def get_price(self):
        return f"The price for the car {self.model} is {self.price}"

    def drive(self):
        return "Driving a car"

class Motorcycle(VehicleSOLID):
    def get_price(self):
        return f"The price for the motorcycle {self.model} is {self.price}"

    def ride(self):
        return "Riding a motorcycle"

# Instanciando objetos
vehicle = Vehicle("car", "Toyota", 20000)
car = Car("Honda", 15000)
motorcycle = Motorcycle("Yamaha", 5000)

(vehicle.get_price(), vehicle.drive(), car.get_price(), car.drive(), motorcycle.get_price(), motorcycle.ride())
