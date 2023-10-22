"""seasons = ("Winter", "Spring", "Summer", "Autumn", "Winter")

try:
    month_number = int(input("Enter a month number (1-12): "))
    if 1 <= month_number <= 12:
        season = seasons[(month_number - 1) // 3]
        print(f"The season corresponding to month {month_number} is {season}.")
    else:
        print("Invalid input. Please enter a month number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter a valid month number.")"""

"""names = set()
input_names = []

while True:
    name = input("Enter a name (or press Enter to finish): ")

    if not name:
        break  # Exit the loop if the user enters an empty string

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

    input_names.append(name)

print("List of input names:")
for name in input_names:

    print(name)"""


"""airport_data = {}

while True:
    print("Choose an option:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        icao_code = input("Enter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")
        airport_data[icao_code] = airport_name
        print(f"Airport data for {icao_code} added successfully.")

    elif choice == "2":
        icao_code = input("Enter the ICAO code of the airport to fetch: ")
        if icao_code in airport_data:
            print(f"The name of the airport with ICAO code {icao_code} is: {airport_data[icao_code]}")
        else:
            print(f"No information found for ICAO code {icao_code}.")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")"""