from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)


def display_weather(data):

    city = data["name"]
    country = data["sys"]["country"]

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    description = data["weather"][0]["description"].title()

    wind_speed = data["wind"]["speed"]

    visibility = data["visibility"] / 1000

    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"]
    ).strftime("%I:%M %p")

    sunset = datetime.fromtimestamp(
        data["sys"]["sunset"]
    ).strftime("%I:%M %p")

    print(Fore.CYAN + "-" * 55)

    print(Fore.YELLOW + f"📍 City         : {city}, {country}")
    print(Fore.RED + f"🌡 Temperature  : {temperature} °C")
    print(Fore.RED + f"🥵 Feels Like   : {feels_like} °C")
    print(Fore.BLUE + f"📉 Min Temp     : {temp_min} °C")
    print(Fore.MAGENTA + f"📈 Max Temp     : {temp_max} °C")
    print(Fore.WHITE + f"☁ Condition    : {description}")
    print(Fore.CYAN + f"💧 Humidity     : {humidity}%")
    print(Fore.GREEN + f"🌬 Wind Speed   : {wind_speed} m/s")
    print(Fore.YELLOW + f"📊 Pressure     : {pressure} hPa")
    print(Fore.BLUE + f"👁 Visibility   : {visibility} km")
    print(Fore.LIGHTYELLOW_EX + f"🌅 Sunrise      : {sunrise}")
    print(Fore.LIGHTRED_EX + f"🌇 Sunset       : {sunset}")

    print(Fore.CYAN + "-" * 55)