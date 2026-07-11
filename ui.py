# ==========================================
# Weather App User Interface
# ==========================================


from weather import get_weather

from dashboard import display_dashboard

from favorites import (
    add_favorite,
    get_favorites,
    remove_favorite
)

from history import (
    save_history,
    get_history,
    clear_history
)

from loading import show_loading

from utils import welcome_message





# ------------------------------------------
# Search Weather Function
# ------------------------------------------


def search_weather():


    city = input(
        "\nEnter city name: "
    )


    if not city:


        print(
            "City name cannot be empty"
        )

        return




    show_loading()



    weather, error = get_weather(city)



    if error:


        print(
            "\n⚠ Error:",
            error
        )


        return





    # Save search history

    save_history(city)




    # Display dashboard

    display_dashboard(weather)





    choice = input(

        "\nAdd this city to favourites? (y/n): "

    )



    if choice.lower() == "y":


        if add_favorite(city):


            print(
                "⭐ Added to favourites"
            )


        else:


            print(
                "Already in favourites"
            )







# ------------------------------------------
# Show Search History
# ------------------------------------------


def show_history_menu():


    history = get_history()



    print("\n===== SEARCH HISTORY =====")



    if not history:


        print(
            "No search history found"
        )


        return




    for index, city in enumerate(history,1):


        print(

            f"{index}. {city}"

        )







# ------------------------------------------
# Show Favourite Cities
# ------------------------------------------


def show_favorites_menu():


    favorites = get_favorites()



    print("\n===== FAVOURITE CITIES =====")



    if not favorites:


        print(
            "No favourites added"
        )


        return





    for index, city in enumerate(favorites,1):


        print(

            f"{index}. ⭐ {city}"

        )








# ------------------------------------------
# Remove Favourite
# ------------------------------------------


def remove_favorite_menu():


    city = input(

        "\nEnter city to remove: "

    )



    if remove_favorite(city):


        print(
            "Removed successfully"
        )


    else:


        print(
            "City not found"
        )








# ------------------------------------------
# Main Application Menu
# ------------------------------------------


def start_ui():


    print(

        welcome_message()

    )



    while True:



        print("""

=====================================
            WEATHER APP PRO
=====================================

1. Search Weather

2. Search History

3. Favourite Cities

4. Remove Favourite

5. Clear History

6. Exit

=====================================

""")



        choice = input(

            "Enter your choice: "

        )






        if choice == "1":


            search_weather()






        elif choice == "2":


            show_history_menu()






        elif choice == "3":


            show_favorites_menu()






        elif choice == "4":


            remove_favorite_menu()






        elif choice == "5":


            clear_history()


            print(
                "History cleared"
            )






        elif choice == "6":


            print(

                "Thank you for using Weather App Pro"

            )


            break





        else:


            print(

                "Invalid option"

            )