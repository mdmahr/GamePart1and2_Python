"""import random

def roll_dice():
    return random.randint(1, 6)

def main():
    rolls = 0
    while True:
        result = roll_dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")
        if result == 6:
            break

main()"""


"""import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    max_sides = int(input("Enter the number of sides on the dice: "))
    rolls = 0
    while True:
        result = roll_dice(max_sides)
        rolls += 1
        print(f"Roll {rolls}: {result}")
        if result == max_sides:
            break

main()"""



"""def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

while True:
    try:
        gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
        if gallons < 0:
            print("Program ended.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters} liters")
    except ValueError:
        print("Invalid input. Please enter a valid number.")"""


"""def sum_of_list(numbers):
    total = sum(numbers)
    return total

# Main program for testing
if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5]  # You can modify this list with your own integers
    result = sum_of_list(num_list)
    print(f"The sum of the numbers in the list is: {result}")"""


"""def remove_odd_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # You can modify this list with your own integers
    modified_list = remove_odd_numbers(num_list)

    print("Original list:", num_list)
    print("Modified list with odd numbers removed:", modified_list)"""

"""import math


def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    unit_price = price / area
    return unit_price


def main():
    diameter1 = float(input("Enter the diameter of the first pizza (in centimeters): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))

    diameter2 = float(input("Enter the diameter of the second pizza (in centimeters): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))

    unit_price1 = unit_price(diameter1, price1)
    unit_price2 = unit_price(diameter2, price2)

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")


main()"""







