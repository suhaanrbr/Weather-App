"""
utils.py
Utility functions for Weather App Pro
"""

import os
from datetime import datetime
from PIL import Image
import customtkinter as ctk

from config import (
    WEATHER_ICONS,
    WEATHER_COLORS,
    DEFAULT_COLOR,
    ASSETS_PATH,
    ICON_SIZE
)


# ==========================================================
# TEMPERATURE
# ==========================================================

def temperature(value):

    try:
        return f"{round(float(value))}°C"
    except:
        return "--"


# ==========================================================
# HUMIDITY
# ==========================================================

def humidity(value):

    try:
        return f"{int(value)}%"
    except:
        return "--"


# ==========================================================
# PRESSURE
# ==========================================================

def pressure(value):

    try:
        return f"{int(value)} hPa"
    except:
        return "--"


# ==========================================================
# WIND
# ==========================================================

def wind(value):

    try:
        return f"{float(value):.1f} m/s"
    except:
        return "--"


# ==========================================================
# VISIBILITY
# ==========================================================

def visibility(value):

    try:
        return f"{float(value):.1f} km"
    except:
        return "--"


# ==========================================================
# WEATHER DESCRIPTION
# ==========================================================

def description(text):

    if not text:
        return "Unknown"

    return text.title()


# ==========================================================
# CURRENT DATE
# ==========================================================

def current_date():

    return datetime.now().strftime("%A, %d %B %Y")


# ==========================================================
# CURRENT TIME
# ==========================================================

def current_time():

    return datetime.now().strftime("%I:%M:%S %p")


# ==========================================================
# GREETING
# ==========================================================

def greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning"

    if hour < 17:
        return "Good Afternoon"

    return "Good Evening"


# ==========================================================
# WEATHER COLOR
# ==========================================================

def weather_color(weather):

    return WEATHER_COLORS.get(weather, DEFAULT_COLOR)


# ==========================================================
# WEATHER ICON PATH
# ==========================================================

def weather_icon_path(weather):

    filename = WEATHER_ICONS.get(weather, "clouds.png")

    return os.path.join(
        ASSETS_PATH,
        filename
    )


# ==========================================================
# LOAD PNG ICON
# ==========================================================

def load_icon(weather):

    path = weather_icon_path(weather)

    if not os.path.exists(path):
        return None

    image = Image.open(path)

    return ctk.CTkImage(
        light_image=image,
        dark_image=image,
        size=ICON_SIZE
    )


# ==========================================================
# CARD COLOR
# ==========================================================

def card_color(weather):

    color = weather_color(weather)

    return color


# ==========================================================
# VALIDATE CITY
# ==========================================================

def valid_city(city):

    if city is None:
        return False

    city = city.strip()

    if city == "":
        return False

    return True


# ==========================================================
# CAPITALIZE CITY
# ==========================================================

def clean_city(city):

    return city.strip().title()


# ==========================================================
# FILE EXISTS
# ==========================================================

def file_exists(path):

    return os.path.exists(path)


# ==========================================================
# CREATE FILE
# ==========================================================

def create_file(path):

    if not os.path.exists(path):

        with open(path, "w", encoding="utf-8"):
            pass


# ==========================================================
# APP VERSION
# ==========================================================

def version():

    return "Weather App Pro v2.0"


# ==========================================================
# AUTHOR
# ==========================================================

def author():

    return "Waqar Younis"


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    print(greeting())

    print(current_date())

    print(current_time())

    print(weather_icon_path("Clear"))