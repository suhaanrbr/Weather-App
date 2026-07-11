HISTORY_FILE = "history.txt"


def save_city(city):
    with open(HISTORY_FILE, "a") as file:
        file.write(city + "\n")


def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            cities = file.readlines()

            if not cities:
                print("\nNo search history found.")
                return

            print("\n========== Search History ==========")

            for index, city in enumerate(cities, start=1):
                print(f"{index}. {city.strip()}")

            print("====================================")

    except FileNotFoundError:
        print("\nNo search history found.")


def clear_history():
    with open(HISTORY_FILE, "w") as file:
        pass

    print("\nHistory cleared successfully.")