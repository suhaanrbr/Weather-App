from datetime import datetime
import os


def count_lines(filename):

    if not os.path.exists(filename):
        return 0

    with open(filename, "r") as file:
        return len(file.readlines())


def show_dashboard():

    today = datetime.now()

    favorites = count_lines("favorites.txt")
    history = count_lines("history.txt")

    print("=" * 60)
    print("🌦️           WEATHER APPLICATION")
    print("=" * 60)

    print(f"📅 Date : {today.strftime('%d %B %Y')}")
    print(f"🕒 Time : {today.strftime('%I:%M:%S %p')}")

    print("-" * 60)

    print(f"⭐ Favorite Cities : {favorites}")
    print(f"📜 Search History : {history}")

    print("-" * 60)

    print("1. Search Weather")
    print("2. View Search History")
    print("3. Clear History")
    print("4. View Favorite Cities")
    print("5. Add Favorite City")
    print("6. Remove Favorite City")
    print("7. Exit")

    print("=" * 60)