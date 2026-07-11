from ui import show_title
from utils import line
from weather import get_weather
from history import save_history, show_history

while True:

    show_title()

    print("1. Search Weather")
    print("2. View Search History")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        city = input("\nEnter your city: ")

        weather = get_weather(city)

        line()

        if weather:

            save_history(city)

            print("\n========== WEATHER REPORT ==========\n")

            print(f"{weather['icon']} Weather      : {weather['condition'].title()}")
            print(f"📍 City         : {weather['city']}, {weather['country']}")
            print(f"🌡 Temperature  : {weather['temperature']} °C")
            print(f"🥵 Feels Like   : {weather['feels_like']} °C")
            print(f"💧 Humidity     : {weather['humidity']}%")
            print(f"🌬 Wind Speed   : {weather['wind']} m/s")

            print("\n===================================")

        else:
            print("❌ City not found.")

        line()

        input("\nPress Enter to continue...")

    elif choice == "2":

        show_history()

        input("\nPress Enter to continue...")

    elif choice == "3":

        print("\n👋 Goodbye!")
        break

    else:

        print("\nInvalid option.")

        input("\nPress Enter to continue...")