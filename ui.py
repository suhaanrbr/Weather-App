from datetime import datetime


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

    print("-" * 50)

    print(f"📍 City         : {city}, {country}")
    print(f"🌡 Temperature  : {temperature} °C")
    print(f"🥵 Feels Like  : {feels_like} °C")
    print(f"📉 Min Temp     : {temp_min} °C")
    print(f"📈 Max Temp     : {temp_max} °C")
    print(f"☁ Condition    : {description}")
    print(f"💧 Humidity     : {humidity}%")
    print(f"🌬 Wind Speed   : {wind_speed} m/s")
    print(f"📊 Pressure     : {pressure} hPa")
    print(f"👁 Visibility   : {visibility} km")
    print(f"🌅 Sunrise      : {sunrise}")
    print(f"🌇 Sunset       : {sunset}")

    print("-" * 50)