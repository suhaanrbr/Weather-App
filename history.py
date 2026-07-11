def save_history(city):

    with open("history.txt", "a") as file:
        file.write(city + "\n")


def show_history():

    try:

        with open("history.txt", "r") as file:

            history = file.readlines()

            if len(history) == 0:
                print("\nNo searches found.")
                return

            print("\n========== SEARCH HISTORY ==========\n")

            for number, city in enumerate(history, start=1):
                print(f"{number}. {city.strip()}")

    except FileNotFoundError:
        print("\nNo history found.")