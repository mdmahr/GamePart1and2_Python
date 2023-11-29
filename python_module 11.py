"""class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        raise NotImplementedError("Subclasses must implement this method")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


if __name__ == "__main__":

    donald_duck_magazine = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
    compartment_no_6_book = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)


    donald_duck_magazine.print_information()
    print("\n-----------------\n")
    compartment_no_6_book.print_information()"""


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        new_speed = self.speed + speed_change
        self.speed = max(0, min(new_speed, self.max_speed))

    def drive(self, hours):
        distance_covered = self.speed * hours
        self.distance_traveled += distance_covered


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

    def print_information(self):
        print(f"Electric Car ({self.registration_number}): Max Speed - {self.max_speed} km/h, Battery Capacity - {self.battery_capacity} kWh")


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

    def print_information(self):
        print(f"Gasoline Car ({self.registration_number}): Max Speed - {self.max_speed} km/h, Tank Volume - {self.tank_volume} liters")

if __name__ == "__main__":

    electric_car = ElectricCar(registration_number="ABC-15", max_speed=180, battery_capacity=52.5)

    gasoline_car = GasolineCar(registration_number="ACD-123", max_speed=165, tank_volume=32.3)

    electric_car.accelerate(30)  # Speeding up the electric car by 30 km/h
    gasoline_car.accelerate(20)  # Speeding up the gasoline car by 20 km/h

    electric_car.drive(3)
    gasoline_car.drive(3)

    print(f"Electric Car Distance Traveled: {electric_car.distance_traveled} km")
    print(f"Gasoline Car Distance Traveled: {gasoline_car.distance_traveled} km")

    electric_car.print_information()
    gasoline_car.print_information()

