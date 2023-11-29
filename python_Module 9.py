class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

def main():

    new_car = Car(registration_number="ABC-123", max_speed=142)

    print("Car Details:")
    print("Registration Number:", new_car.registration_number)
    print("Maximum Speed:", new_car.max_speed, "km/h")
    print("Current Speed:", new_car.current_speed, "km/h")
    print("Travelled Distance:", new_car.travelled_distance, "km")

if __name__ == "__main__":
    main()


class Car:
    def __init__(self, make, model, max_speed):
        self.make = make
        self.model = model
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, speed_change):
        new_speed = self.speed + speed_change
        self.speed = max(0, min(new_speed, self.max_speed))

my_car = Car("Toyota", "Camry", 200)

my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)

print("Current speed after acceleration:", my_car.speed, "km/h")

my_car.accelerate(-200)

print("Final speed after emergency brake:", my_car.speed, "km/h")



class Car:
    def __init__(self, make, model, max_speed):
        self.make = make
        self.model = model
        self.max_speed = max_speed
        self.speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        new_speed = self.speed + speed_change
        self.speed = max(0, min(new_speed, self.max_speed))

    def drive(self, hours):
        # Calculate the distance traveled in constant speed
        distance_covered = self.speed * hours
        # Update the total distance traveled
        self.distance_traveled += distance_covered

my_car = Car("Toyota", "Camry", 200)

my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)

print("Current speed after acceleration:", my_car.speed, "km/h")

my_car.drive(1.5)

print("Distance traveled after driving for 1.5 hours:", my_car.distance_traveled, "km")





import random

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

cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

while all(car.distance_traveled < 10000 for car in cars):
    # Simulate one hour of the race
    for car in cars:
        # Change speed by a random value between -10 and +15 km/h
        car.accelerate(random.randint(-10, 15))
        # Drive for one hour
        car.drive(1)

print("{:<12} {:<15} {:<15} {:<20}".format("Car Number", "Max Speed (km/h)", "Distance Traveled (km)", "Final Speed (km/h)"))
print("-" * 65)

for car in cars:
    print("{:<12} {:<15} {:<15} {:<20}".format(car.registration_number, car.max_speed, car.distance_traveled, car.speed))




