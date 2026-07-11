from colorama import Fore, Style, init

from weather import get_weather
from ui import display_weather
from loading import loading
from history import save_city, show_history, clear_history

init(autoreset=True)


def main():

    print(Fore.CYAN + "=" * 55)
    print(Fore.YELLOW + Style.BRIGHT + "🌦️ WEATHER APPLICATION")
    print(Fore.CYAN + "=" * 55)

    while True:

        print("\n1. Search Weather")
        print("2. View Search History")
        print("3. Clear History")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            city = input("\nEnter city name: ").strip()

            loading()

            weather = get_weather(city)

            if weather:

                save_city(city.title())

                display_weather(weather)

        elif choice == "2":

            show_history()

        elif choice == "3":

            clear_history()

        elif choice == "4":

            print(Fore.MAGENTA + "\n👋 Goodbye!")
            break

        else:

            print(Fore.RED + "\nInvalid option.")
            

if __name__ == "__main__":
    main()