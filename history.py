"""
history.py
Manage search history.
"""

import os
from datetime import datetime
from config import HISTORY_FILE


# ==========================================================
# CREATE FILE
# ==========================================================

def initialize_history():

    if not os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "w", encoding="utf-8"):
            pass


initialize_history()


# ==========================================================
# SAVE HISTORY
# ==========================================================

def save_history(city):

    city = city.title()

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:

        file.write(f"{city}|{current_time}\n")


# ==========================================================
# GET HISTORY
# ==========================================================

def get_history():

    history = []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:

        for line in file.readlines():

            line = line.strip()

            if not line:
                continue

            try:

                city, timestamp = line.split("|", 1)

            except ValueError:

                city = line
                timestamp = ""

            history.append({

                "city": city,

                "time": timestamp

            })

    history.reverse()

    return history


# ==========================================================
# LAST SEARCH
# ==========================================================

def last_search():

    history = get_history()

    if history:

        return history[0]["city"]

    return None


# ==========================================================
# CLEAR HISTORY
# ==========================================================

def clear_history():

    with open(HISTORY_FILE, "w", encoding="utf-8"):
        pass


# ==========================================================
# DELETE ONE ENTRY
# ==========================================================

def delete_history(city):

    city = city.title()

    history = get_history()

    history = [

        item

        for item in history

        if item["city"] != city

    ]

    history.reverse()

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:

        for item in history:

            file.write(

                f"{item['city']}|{item['time']}\n"

            )


# ==========================================================
# TOTAL SEARCHES
# ==========================================================

def total_searches():

    return len(get_history())


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    print(get_history())