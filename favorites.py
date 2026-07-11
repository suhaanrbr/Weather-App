FAVORITES_FILE = "favorites.txt"


def add_favorite(city):

    city = city.title()

    try:
        with open(FAVORITES_FILE, "r") as file:
            favorites = [line.strip() for line in file]

        if city in favorites:
            print("\n⭐ City already exists in favorites.")
            return

    except FileNotFoundError:
        pass

    with open(FAVORITES_FILE, "a") as file:
        file.write(city + "\n")

    print(f"\n✅ {city} added to favorites.")


def show_favorites():

    try:
        with open(FAVORITES_FILE, "r") as file:
            favorites = file.readlines()

        if not favorites:
            print("\nNo favorite cities.")
            return

        print("\n========== Favorite Cities ==========")

        for index, city in enumerate(favorites, start=1):
            print(f"{index}. {city.strip()}")

        print("=====================================")

    except FileNotFoundError:
        print("\nNo favorite cities.")


def remove_favorite(city):

    city = city.title()

    try:
        with open(FAVORITES_FILE, "r") as file:
            favorites = [line.strip() for line in file]

        if city not in favorites:
            print("\nCity not found.")
            return

        favorites.remove(city)

        with open(FAVORITES_FILE, "w") as file:
            for item in favorites:
                file.write(item + "\n")

        print(f"\n🗑 {city} removed from favorites.")

    except FileNotFoundError:
        print("\nNo favorite cities.")