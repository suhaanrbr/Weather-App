import requests
from config import API_KEY, BASE_URL
from datetime import datetime


def get_weather(city):

    try:

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }


        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )


        if response.status_code == 404:
            return None, "City not found"


        if response.status_code == 401:
            return None, "Invalid API Key"


        response.raise_for_status()


        data = response.json()


        weather = {

            "city": data["name"],

            "country": data["sys"]["country"],

            "temperature": data["main"]["temp"],

            "feels_like": data["main"]["feels_like"],

            "min_temp": data["main"]["temp_min"],

            "max_temp": data["main"]["temp_max"],

            "humidity": data["main"]["humidity"],

            "pressure": data["main"]["pressure"],

            "wind": data["wind"]["speed"],

            "visibility": data.get("visibility",0)/1000,

            "description":
            data["weather"][0]["description"],


            "sunrise":
            datetime.fromtimestamp(
                data["sys"]["sunrise"]
            ).strftime("%I:%M %p"),


            "sunset":
            datetime.fromtimestamp(
                data["sys"]["sunset"]
            ).strftime("%I:%M %p")

        }


        return weather, None



    except requests.exceptions.Timeout:

        return None,"Request timeout"


    except requests.exceptions.ConnectionError:

        return None,"No internet connection"



    except Exception as e:

        return None,str(e)