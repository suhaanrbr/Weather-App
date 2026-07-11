def save_history(city):

    with open("history.txt", "a") as file:
        file.write(city + "\n")