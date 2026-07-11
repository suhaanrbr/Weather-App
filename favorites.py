"""
favorites.py
Manage favourite cities.
"""

import os
from config import FAVORITES_FILE


# ==========================================================
# CREATE FILE
# ==========================================================

def initialize_favorites():

    if not os.path.exists(FAVORITES_FILE):

        with open(FAVORITES_FILE, "w", encoding="utf-8"):
            pass


initialize_favorites()


# ==========================================================
# GET FAVORITES
# ==========================================================

def get_favorites():

    with open(FAVORITES_FILE, "r", encoding="utf-8") as file:

        favorites = [
            city.strip()
            for city in file.readlines()
            if city.strip()
        ]

    return favorites


# ==========================================================
# ADD FAVORITE
# ==========================================================

def add_favorite(city):

    city = city.title()

    favorites = get_favorites()

    if city in favorites:
        return False

    with open(FAVORITES_FILE, "a", encoding="utf-8") as file:

        file.write(city + "\n")

    return True


# ==========================================================
# REMOVE FAVORITE
# ==========================================================

def remove_favorite(city):

    city = city.title()

    favorites = get_favorites()

    if city not in favorites:
        return False

    favorites.remove(city)

    with open(FAVORITES_FILE, "w", encoding="utf-8") as file:

        for favorite in favorites:

            file.write(favorite + "\n")

    return True


# ==========================================================
# CLEAR FAVORITES
# ==========================================================

def clear_favorites():

    with open(FAVORITES_FILE, "w", encoding="utf-8"):
        pass


# ==========================================================
# CHECK FAVORITE
# ==========================================================

def is_favorite(city):

    city = city.title()

    return city in get_favorites()


# ==========================================================
# COUNT
# ==========================================================

def total_favorites():

    return len(get_favorites())


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    print(get_favorites())