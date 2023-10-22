"""number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1"""

"""while True:
    a =  float(input("Enter inches: "))
    if a < 0:
        print("The program ends.")
        a += 1
        break
    else:
        num = a * 2.54

        print(num)"""

"""numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break  # Exit the loop if the user enters an empty string

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")"""



"""import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess the number (between 1 and 10): "))
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
        elif guess < target_number:
            print("Too low. Try again.")
        elif guess > target_number:
            print("Too high. Try again.")
        else:
            print("Correct! You guessed the number.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"The target number was {target_number}.")"""


"""correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Access denied. Please try again.")
        attempts += 1

if attempts >= 5:
    print("Access denied after 5 failed attempts.")"""


import random
Num = int(input("How many random points to generate?: "))
n = 0
i = 0
while  i < Num :
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)

    if x*2 + y*2 < 1.0:
        n += 1

    i += 1

import math

pi = 4.0 * n/Num
print(f"Pi is {pi}, error {math.pi - pi}")

