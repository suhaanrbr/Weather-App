"""
weather.py
Handles current weather and 5-day forecast using OpenWeather API.
"""

import requests
from datetime import datetime

from config import (
    API_KEY,
    CURRENT_WEATHER_URL,
    FORECAST_URL,
    UNITS,
    LANGUAGE,
    REQUEST_TIMEOUT,
)


# ==========================================================
# TIME FORMAT
# ==========================================================

def unix_to_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%I:%M %p")


# ==========================================================
# DATE FORMAT
# ==========================================================

def format_date(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    return date.strftime("%a")


# ==========================================================
# CURRENT WEATHER
# ==========================================================

def get_weather(city):
    """
    Returns:
        weather_data, None
        None, error_message
    """

    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": UNITS,
        "lang": LANGUAGE,
    }

    try:

        response = requests.get(
            CURRENT_WEATHER_URL,
            params=parameters,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        data = response.json()

        weather = {

            "city": data["name"],

            "country": data["sys"]["country"],

            "temperature": round(data["main"]["temp"]),

            "feels_like": round(data["main"]["feels_like"]),

            "temp_min": round(data["main"]["temp_min"]),

            "temp_max": round(data["main"]["temp_max"]),

            "humidity": data["main"]["humidity"],

            "pressure": data["main"]["pressure"],

            "visibility": round(data.get("visibility", 0) / 1000, 1),

            "wind_speed": data["wind"]["speed"],

            "wind_degree": data["wind"].get("deg", 0),

            "description": data["weather"][0]["description"].title(),

            "main": data["weather"][0]["main"],

            "icon": data["weather"][0]["icon"],

            "sunrise": unix_to_time(data["sys"]["sunrise"]),

            "sunset": unix_to_time(data["sys"]["sunset"]),

            "latitude": data["coord"]["lat"],

            "longitude": data["coord"]["lon"],

        }

        return weather, None

    except requests.exceptions.HTTPError:

        return None, "City not found."

    except requests.exceptions.ConnectionError:

        return None, "No internet connection."

    except requests.exceptions.Timeout:

        return None, "Server timeout."

    except Exception as error:

        return None, str(error)


# ==========================================================
# 5-DAY FORECAST
# ==========================================================

def get_forecast(city):
    """
    Returns:
        forecast_list, None
        None, error
    """

    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": UNITS,
        "lang": LANGUAGE,
    }

    try:

        response = requests.get(
            FORECAST_URL,
            params=parameters,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        data = response.json()

        forecast = []

        # Every 8th record ≈ 24 hours
        for item in data["list"][::8]:

            forecast.append({

                "day": format_date(item["dt_txt"]),

                "temperature": round(item["main"]["temp"]),

                "temp_min": round(item["main"]["temp_min"]),

                "temp_max": round(item["main"]["temp_max"]),

                "description": item["weather"][0]["description"].title(),

                "main": item["weather"][0]["main"],

                "icon": item["weather"][0]["icon"]

            })

        return forecast[:5], None

    except Exception as error:

        return None, str(error)


# ==========================================================
# INTERNET CHECK
# ==========================================================

def internet_available():

    try:

        requests.get(
            "https://www.google.com",
            timeout=5
        )

        return True

    except:

        return False


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    city = input("Enter City: ")

    weather, error = get_weather(city)

    if error:
        print(error)

    else:

        print(weather)

        forecast, _ = get_forecast(city)

        print("\nForecast\n")

        for day in forecast:

            print(day)