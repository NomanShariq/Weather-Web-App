import os
from pprint import pprint
from dotenv import load_dotenv
import requests


load_dotenv()


def get_current_weather(city="Karachi"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather ***\n")

    city = input("\nPlease Enter you city:\n")

    # Check for empty strings or string with only spaces

    if not bool(city.strip()):
        city = "Karachi"

    weather_data = get_current_weather(city)

    print("\n")
    print(weather_data)
