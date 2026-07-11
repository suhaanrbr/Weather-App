import requests
from config import API_KEY


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 404:
            print("\n❌ City not found.")
            return None

        else:
            print(f"\n❌ Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException:
        print("\n❌ Internet connection problem.")
        return None