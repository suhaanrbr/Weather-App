from colorama import Fore, Style, init

from weather import get_weather
from ui import display_weather
from loading import loading

from history import (
    save_city,
    show_history,
    clear_history,
)

from favorites import (
    add_favorite,
    show_favorites,
    remove_favorite,
)

init(autoreset=True)


def main():

    print(Fore.CYAN + "=" * 55)
    print(Fore.YELLOW + Style.BRIGHT + "🌦️ WEATHER APPLICATION")
    print(Fore.CYAN + "=" * 55)

    while True:

        print("\n1. Search Weather")
        print("2. View Search History")
        print("3. Clear History")
        print("4. View Favorite Cities")
        print("5. Add Favorite City")
        print("6. Remove Favorite City")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            city = input("\nEnter city name: ")

            loading()

            weather = get_weather(city)

            if weather:

                save_city(city)

                display_weather(weather)

        elif choice == "2":

            show_history()

        elif choice == "3":

            clear_history()

        elif choice == "4":

            show_favorites()

        elif choice == "5":

            city = input("\nCity to add: ")

            add_favorite(city)

        elif choice == "6":

            city = input("\nCity to remove: ")

            remove_favorite(city)

        elif choice == "7":

            print(Fore.GREEN + "\nThanks for using Weather Application!")

            break

        else:

            print(Fore.RED + "\nInvalid option.")


if __name__ == "__main__":
    main()