from ui import show_title
from utils import line
from weather import get_weather
from history import save_history

show_title()

while True:

    city = input("\nEnter your city (or type 'exit'): ")

    if city.lower() == "exit":
        print("\n👋 Thank you for using Weather Application!")
        break

    weather = get_weather(city)

    line()

    if weather:

        save_history(city)

        print(f"📍 City        : {weather['city']}, {weather['country']}")
        print(f"🌡 Temperature : {weather['temperature']} °C")
        print(f"🥵 Feels Like  : {weather['feels_like']} °C")
        print(f"💧 Humidity    : {weather['humidity']}%")
        print(f"☁ Condition   : {weather['condition'].title()}")
        print(f"🌬 Wind Speed  : {weather['wind']} m/s")

    else:
        print("❌ City not found.")

    line()