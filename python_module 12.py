import requests

def get_random_chuck_norris_joke():
    api_url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for errors in the response
        data = response.json()
        return data["value"]
    except requests.RequestException as e:
        print(f"Error fetching Chuck Norris joke: {e}")
        return None

def main():
    joke = get_random_chuck_norris_joke()

    if joke:
        print("Chuck Norris Joke:")
        print(joke)
    else:
        print("Failed to fetch Chuck Norris joke.")

if __name__ == "__main__":
    main()


"""import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if "weather" in data and "main" in data:
            weather_description = data["weather"][0]["description"]
            temperature_kelvin = data["main"]["temp"]
            temperature_celsius = kelvin_to_celsius(temperature_kelvin)

            return weather_description, temperature_celsius
        else:
            print("Invalid data received from the API.")
            return None, None
    except requests.RequestException as e:
        print(f"Error fetching weather information: {e}")
        return None, None

def main():
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    city_name = input("Enter the name of the municipality: ")

    weather_description, temperature_celsius = get_weather(api_key, city_name)

    if weather_description is not None and temperature_celsius is not None:
        print(f"Weather in {city_name}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")

if __name__ == "__main__":
    main()"""

