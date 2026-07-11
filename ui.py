from datetime import datetime
from colorama import Fore, init

init(autoreset=True)


def get_weather_icon(condition):

    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Smoke": "🌫️",
        "Haze": "🌫️",
        "Dust": "🌪️",
        "Fog": "🌫️",
        "Sand": "🏜️",
        "Ash": "🌋",
        "Squall": "💨",
        "Tornado": "🌪️"
    }

    return icons.get(condition, "🌍")


def display_weather(data):

    city = data["name"]
    country = data["sys"]["country"]

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]

    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    main_condition = data["weather"][0]["main"]
    description = data["weather"][0]["description"].title()

    wind_speed = data["wind"]["speed"]

    visibility = data["visibility"] / 1000

    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"]
    ).strftime("%I:%M %p")

    sunset = datetime.fromtimestamp(
        data["sys"]["sunset"]
    ).strftime("%I:%M %p")

    icon = get_weather_icon(main_condition)

    print(Fore.CYAN + "-" * 60)

    print(Fore.YELLOW + f"📍 City         : {city}, {country}")
    print(Fore.RED + f"🌡 Temperature  : {temperature:.1f} °C")
    print(Fore.RED + f"🥵 Feels Like   : {feels_like:.1f} °C")
    print(Fore.BLUE + f"📉 Min Temp     : {temp_min:.1f} °C")
    print(Fore.MAGENTA + f"📈 Max Temp     : {temp_max:.1f} °C")

    print(Fore.WHITE + f"{icon} Weather      : {description}")

    print(Fore.CYAN + f"💧 Humidity     : {humidity}%")
    print(Fore.GREEN + f"🌬 Wind Speed   : {wind_speed} m/s")
    print(Fore.YELLOW + f"📊 Pressure     : {pressure} hPa")
    print(Fore.BLUE + f"👁 Visibility   : {visibility:.1f} km")
    print(Fore.LIGHTYELLOW_EX + f"🌅 Sunrise      : {sunrise}")
    print(Fore.LIGHTRED_EX + f"🌇 Sunset       : {sunset}")

    print(Fore.CYAN + "-" * 60)