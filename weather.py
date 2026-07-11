import requests
from colorama import Fore
from config import API_KEY


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 404:
            print(Fore.RED + "\n❌ City not found.")
            return None

        else:
            print(Fore.RED + f"\n❌ Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException:
        print(Fore.RED + "\n❌ No internet connection.")
        return None