from datetime import datetime


def save_history(data):

    with open("history.txt", "a", encoding="utf-8") as file:

        file.write(

            f"{datetime.now()} | "

            f"{data['name']} | "

            f"{data['main']['temp']}°C | "

            f"{data['weather'][0]['description']}\n"

        )