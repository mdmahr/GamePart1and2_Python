"""class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor request. The floor is out of range.")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving up. Current floor: {self.current_floor}")
        else:
            print("Already on the top floor. Cannot go up.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving down. Current floor: {self.current_floor}")
        else:
            print("Already on the bottom floor. Cannot go down.")

elevator = Elevator(bottom_floor=1, top_floor=10)

elevator.go_to_floor(5)

elevator.go_to_floor(1)"""


"""class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor request. The floor is out of range.")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving up. Current floor: {self.current_floor}")
        else:
            print("Already on the top floor. Cannot go up.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving down. Current floor: {self.current_floor}")
        else:
            print("Already on the bottom floor. Cannot go down.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"\nRunning Elevator {elevator_number} to Floor {destination_floor}")
        elevator.go_to_floor(destination_floor)

building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

building.run_elevator(1, 7)
building.run_elevator(2, 3)
building.run_elevator(3, 9)"""


"""class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor request. The floor is out of range.")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving up. Current floor: {self.current_floor}")
        else:
            print("Already on the top floor. Cannot go up.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving down. Current floor: {self.current_floor}")
        else:
            print("Already on the bottom floor. Cannot go down.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"\nRunning Elevator {elevator_number} to Floor {destination_floor}")
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\nFire alarm activated. Moving all elevators to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

building.run_elevator(1, 7)
building.run_elevator(2, 3)
building.run_elevator(3, 9)

building.fire_alarm()"""



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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print("\n{:<12} {:<15} {:<15} {:<20}".format("Car Number", "Max Speed (km/h)", "Distance Traveled (km)", "Current Speed (km/h)"))
        print("-" * 65)

        for car in self.cars:
            print("{:<12} {:<15} {:<15} {:<20}".format(car.registration_number, car.max_speed, car.distance_traveled, car.speed))

    def race_finished(self):
        return any(car.distance_traveled >= self.distance for car in self.cars)

# Main program
def main():
    # Create a list of 10 cars with random speeds and registration numbers
    cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

    # Create the Grand Demolition Derby race with a distance of 8000 kilometers
    grand_derby = Race(name="Grand Demolition Derby", distance=8000, cars=cars)

    # Simulate the race progress
    hours_elapsed = 0
    while not grand_derby.race_finished():
        if hours_elapsed % 10 == 0:
            grand_derby.print_status()
        grand_derby.hour_passes()
        hours_elapsed += 1

    # Print final status at the end of the race
    grand_derby.print_status()

if __name__ == "__main__":
    main()




