from weather import get_weather
from ui import display_weather


def main():
    print("=" * 45)
    print("🌦️ WEATHER APPLICATION")
    print("=" * 45)

    while True:
        city = input("\nEnter city name (or type 'exit'): ").strip()

        if city.lower() == "exit":
            print("\n👋 Thank you for using Weather Application!")
            break

        weather_data = get_weather(city)

        if weather_data:
            display_weather(weather_data)
        else:
            print("❌ Unable to fetch weather.")

        choice = input("\nSearch another city? (y/n): ").lower()

        if choice != "y":
            print("\n👋 Goodbye!")
            break


if __name__ == "__main__":
    main()