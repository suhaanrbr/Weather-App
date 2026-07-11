def display_weather(data):

    city = data["name"]
    country = data["sys"]["country"]

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    description = data["weather"][0]["description"].title()

    wind_speed = data["wind"]["speed"]

    print("-" * 45)
    print(f"📍 City        : {city}, {country}")
    print(f"🌡 Temperature : {temperature} °C")
    print(f"🥵 Feels Like : {feels_like} °C")
    print(f"💧 Humidity    : {humidity}%")
    print(f"☁ Condition   : {description}")
    print(f"🌬 Wind Speed  : {wind_speed} m/s")