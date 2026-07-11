from colorama import Fore, Style, init

from weather import get_weather
from ui import display_weather
from loading import loading

init(autoreset=True)


def main():

    print(Fore.CYAN + "=" * 55)
    print(Fore.YELLOW + Style.BRIGHT + "🌦️ WEATHER APPLICATION")
    print(Fore.CYAN + "=" * 55)

    while True:

        city = input(Fore.GREEN + "\nEnter city name (or 'exit'): ").strip()

        if city.lower() == "exit":
            print(Fore.MAGENTA + "\n👋 Thank you for using Weather App!")
            break

        loading()

        weather = get_weather(city)

        if weather:
            display_weather(weather)

        choice = input(
            Fore.CYAN + "\nSearch another city? (y/n): "
        ).lower()

        if choice != "y":
            print(Fore.MAGENTA + "\n👋 Goodbye!")
            break


if __name__ == "__main__":
    main()