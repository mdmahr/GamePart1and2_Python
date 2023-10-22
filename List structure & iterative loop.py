"""import random

try:
    num_dice = int(input("Enter the number of dice to roll: "))
    if num_dice <= 0:
        print("Please enter a positive number of dice.")
    else:
        total_sum = 0
        for _ in range(num_dice):
            roll = random.randint(1, 6)
            total_sum += roll
            print(f"Die {num_dice}: {roll}")
        print(f"Total sum: {total_sum}")
except ValueError:
    print("Invalid input. Please enter a valid number of dice.")"""



"""numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    numbers.sort(reverse=True)
    top_five = numbers[:5]
    print("The five greatest numbers in descending order are:")
    for i, num in enumerate(top_five, start=1):
        print(f"{i}: {num}")
else:
    print("No numbers were entered.")"""


"""def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

try:
    num = int(input("Enter an integer to check if it's a prime number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")"""


"""cities = []

for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities.append(city)

print("The names of the cities are:")
for city in cities:
    print(city)"""



