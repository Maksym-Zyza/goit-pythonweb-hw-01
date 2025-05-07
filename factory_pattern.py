from abc import ABC, abstractmethod


# Abstract base class for all vehicles
class Vehicle(ABC):
    def __init__(self, make, model, region_spec="") -> None:
        self.make = make
        self.model = model
        self.region_spec = region_spec
    
    @abstractmethod
    def start_engine(self):
        pass


# Car and Motorcycle classes implementing start_engine
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} {self.region_spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} {self.region_spec}: Мотор заведено")


# Abstract factory for creating vehicles
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


# Factory for creating vehicles with US specifications
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")


# Factory for creating vehicles with EU specifications
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")


# Create objects using vehicle factories
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

vehicle3 = eu_factory.create_car("Renault", "Duster")
vehicle4 = eu_factory.create_motorcycle("Yamaha", "R1")

# Start engines
vehicle1.start_engine()
vehicle2.start_engine()
vehicle3.start_engine()
vehicle4.start_engine()
