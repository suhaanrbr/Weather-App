from weather import get_weather

print("=" * 40)
print("🌦️ Weather Application")
print("=" * 40)

city = input("Enter your city: ")

weather_data = get_weather(city)

if weather_data["cod"] == 200:

    city_name = weather_data["name"]
    country = weather_data["sys"]["country"]

    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]

    weather = weather_data["weather"][0]["description"]

    wind_speed = weather_data["wind"]["speed"]

    print()
    print(f"📍 City: {city_name}, {country}")
    print(f"🌡️ Temperature: {temperature}°C")
    print(f"🤗 Feels Like: {feels_like}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️ Wind Speed: {wind_speed} m/s")
    print(f"☁️ Weather: {weather.title()}")

else:
    print("❌ City not found.")