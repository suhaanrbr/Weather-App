def add_favorite(city):

    with open("favorites.txt", "a") as file:
        file.write(city + "\n")


def show_favorites():

    try:

        with open("favorites.txt", "r") as file:

            cities = file.readlines()

            if len(cities) == 0:
                print("\nNo favorite cities saved.")
                return

            print("\n⭐ FAVORITE CITIES\n")

            for number, city in enumerate(cities, start=1):
                print(f"{number}. {city.strip()}")

    except FileNotFoundError:
        print("\nNo favorites yet.")