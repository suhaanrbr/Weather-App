from weather import get_weather

from utils import (
    save_history,
    show_history,
    save_favourite,
    get_favourites,
    remove_favourite
)



def display_weather(weather):

    print("\n==============================")

    print(
        f"Weather Report: "
        f"{weather['city']}, {weather['country']}"
    )


    print("==============================")

    print(
        f"Condition : {weather['description']}"
    )

    print(
        f"Temperature : {weather['temperature']} °C"
    )


    print(
        f"Feels Like : {weather['feels_like']} °C"
    )


    print(
        f"Minimum Temp : {weather['min_temp']} °C"
    )


    print(
        f"Maximum Temp : {weather['max_temp']} °C"
    )


    print(
        f"Humidity : {weather['humidity']} %"
    )


    print(
        f"Pressure : {weather['pressure']} hPa"
    )


    print(
        f"Wind Speed : {weather['wind']} m/s"
    )


    print(
        f"Visibility : {weather['visibility']} km"
    )


    print(
        f"Sunrise : {weather['sunrise']}"
    )


    print(
        f"Sunset : {weather['sunset']}"
    )


    print("==============================\n")





def menu():

    while True:


        print("""
========= WEATHER APP =========

1. Search Weather

2. View Search History

3. View Favourite Cities

4. Remove Favourite

5. Exit

===============================
""")


        choice=input("Enter choice: ")



        if choice=="1":


            city=input(
                "\nEnter city name: "
            )


            weather,error=get_weather(city)


            if error:

                print(
                    "\nError:",
                    error
                )

            else:

                display_weather(weather)


                save_history(city)


                fav=input(
                    "Add to favourites? (y/n): "
                )


                if fav.lower()=="y":

                    save_favourite(city)



        elif choice=="2":


            print("\nSearch History:")

            for city in show_history():

                print(
                    city.strip()
                )



        elif choice=="3":


            print("\nFavourite Cities:")

            for city in get_favourites():

                print(city)




        elif choice=="4":


            city=input(
                "Enter city to remove: "
            )


            if remove_favourite(city):

                print(
                    "Removed successfully"
                )

            else:

                print(
                    "City not found"
                )



        elif choice=="5":

            print(
                "Thank you for using Weather App"
            )

            break



        else:

            print(
                "Invalid option"
            )




if __name__=="__main__":

    menu()