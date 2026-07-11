import os


HISTORY_FILE="history.txt"

FAVOURITE_FILE="favourites.txt"



def save_history(city):

    with open(HISTORY_FILE,"a") as file:

        file.write(city+"\n")




def show_history():

    if not os.path.exists(HISTORY_FILE):

        return []


    with open(HISTORY_FILE,"r") as file:

        return file.readlines()




def save_favourite(city):

    favourites=get_favourites()


    if city not in favourites:

        with open(FAVOURITE_FILE,"a") as file:

            file.write(city+"\n")

        return True


    return False




def get_favourites():

    if not os.path.exists(FAVOURITE_FILE):

        return []


    with open(FAVOURITE_FILE,"r") as file:

        return [
            city.strip()
            for city in file.readlines()
        ]




def remove_favourite(city):

    favourites=get_favourites()


    if city in favourites:

        favourites.remove(city)


        with open(FAVOURITE_FILE,"w") as file:

            for item in favourites:

                file.write(item+"\n")

        return True


    return False