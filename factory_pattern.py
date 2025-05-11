from abc import ABC, abstractmethod
from pathlib import Path
import logging

# Cтворюємо логер, рівень INFO
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

# Створюємо файловий handler для логера, рівень ERROR:
filename = Path(__file__).stem
fh = logging.FileHandler(f"{filename}.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(fh)


# Створюємо абстрактний базовий клас Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec="") -> None:
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self):
        pass


# Car та Motorcycle успадковуються від Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} {self.region_spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} {self.region_spec}: Мотор заведено")


# Створюємо абстрактний клас VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


# Реалізуємо USVehicleFactory та EUVehicleFactory. Cтворюють автомобілі та мотоцикли з позначкою регіону
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str):
        return Motorcycle(make, model, "EU Spec")


def main():
    # Використовуються фабрики для створення транспортних засобів
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    vehicle3 = eu_factory.create_car("Renault", "Duster")
    vehicle4 = eu_factory.create_motorcycle("Yamaha", "R1")

    vehicle1.start_engine()
    vehicle2.start_engine()
    vehicle3.start_engine()
    vehicle4.start_engine()


if __name__ == "__main__":
    main()
