from weather import get_weather

print("=" * 40)
print("🌦️ Weather Application")
print("=" * 40)

city = input("Enter your city: ")

weather_data = get_weather(city)

print(weather_data)