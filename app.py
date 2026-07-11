from colorama import Fore, init

from dashboard import show_dashboard
from loading import loading
from weather import get_weather
from ui import display_weather

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

    while True:

        show_dashboard()

        choice = input("\nSelect an option: ")

        if choice == "1":

            city = input("\nEnter city name: ").strip()

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

            city = input("\nCity name: ")

            add_favorite(city)

        elif choice == "6":

            city = input("\nCity name: ")

            remove_favorite(city)

        elif choice == "7":

            print(Fore.GREEN + "\n👋 Thank you for using Weather Application!")

            break

        else:

            print(Fore.RED + "\nInvalid option.")


if __name__ == "__main__":
    main()