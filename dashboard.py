"""
dashboard.py
Weather App Pro Dashboard
"""

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os

from weather import get_weather, get_forecast
from favorites import (
    add_favorite,
    remove_favorite,
    get_favorites
)
from history import (
    save_history,
    get_history,
    clear_history,
    last_search
)
from utils import (
    temperature,
    humidity,
    pressure,
    wind,
    visibility,
    description,
    weather_color,
    load_icon,
    valid_city,
    clean_city,
    current_date,
    current_time,
    greeting
)


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.master = master

        self.current_weather = None
        self.current_forecast = []

        self.configure(
            fg_color="#1b1b1b"
        )

        self.build_ui()

        city = last_search()

        if city:
            self.city_entry.insert(0, city)
            self.search_weather()

    # ==========================================================
    # BUILD UI
    # ==========================================================

    def build_ui(self):

        self.columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            self,
            text="Weather App Pro",
            font=("Segoe UI", 34, "bold")
        )

        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text=greeting(),
            font=("Segoe UI", 18)
        )

        subtitle.pack()

        self.date_label = ctk.CTkLabel(
            self,
            text=current_date(),
            font=("Segoe UI", 15)
        )

        self.date_label.pack()

        self.time_label = ctk.CTkLabel(
            self,
            text=current_time(),
            font=("Segoe UI", 15)
        )

        self.time_label.pack(pady=(0, 20))

        self.search_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.search_frame.pack(
            pady=10
        )

        self.city_entry = ctk.CTkEntry(
            self.search_frame,
            width=350,
            height=40,
            placeholder_text="Enter city..."
        )

        self.city_entry.pack(
            side="left",
            padx=10
        )

        self.city_entry.bind(
            "<Return>",
            lambda event: self.search_weather()
        )

        self.search_button = ctk.CTkButton(
            self.search_frame,
            width=120,
            height=40,
            text="Search",
            command=self.search_weather
        )

        self.search_button.pack(
            side="left",
            padx=10
        )

        self.content = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.content.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.left = ctk.CTkFrame(
            self.content,
            width=300
        )

        self.left.pack(
            side="left",
            fill="y",
            padx=15,
            pady=15
        )

        self.icon_label = ctk.CTkLabel(
            self.left,
            text=""
        )

        self.icon_label.pack(
            pady=(25, 10)
        )

        self.temp_label = ctk.CTkLabel(
            self.left,
            text="--°C",
            font=("Segoe UI", 42, "bold")
        )

        self.temp_label.pack()

        self.city_label = ctk.CTkLabel(
            self.left,
            text="Search a city",
            font=("Segoe UI", 24)
        )

        self.city_label.pack()

        self.desc_label = ctk.CTkLabel(
            self.left,
            text="",
            font=("Segoe UI", 18)
        )

        self.desc_label.pack(
            pady=(0, 20)
        )

        self.feels_label = ctk.CTkLabel(
            self.left,
            text="Feels Like --",
            font=("Segoe UI", 16)
        )

        self.feels_label.pack()

        self.minmax_label = ctk.CTkLabel(
            self.left,
            text="Min --°C   Max --°C",
            font=("Segoe UI", 16)
        )

        self.minmax_label.pack(
            pady=(10, 20)
        )

        self.right = ctk.CTkFrame(
            self.content
        )

        self.right.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.cards = ctk.CTkFrame(
            self.right,
            fg_color="transparent"
        )

        self.cards.pack(
            fill="x",
            pady=10
        )

        self.card_values = {}

        items = [
            "Humidity",
            "Pressure",
            "Wind",
            "Visibility",
            "Sunrise",
            "Sunset"
        ]

        index = 0

        for row in range(2):

            for column in range(3):

                frame = ctk.CTkFrame(
                    self.cards,
                    width=180,
                    height=110
                )

                frame.grid(
                    row=row,
                    column=column,
                    padx=10,
                    pady=10
                )

                title = ctk.CTkLabel(
                    frame,
                    text=items[index],
                    font=("Segoe UI", 15, "bold")
                )

                title.pack(
                    pady=(15, 5)
                )

                value = ctk.CTkLabel(
                    frame,
                    text="--",
                    font=("Segoe UI", 20)
                )

                value.pack()

                self.card_values[
                    items[index]
                ] = value

                index += 1

        self.forecast_title = ctk.CTkLabel(
            self.right,
            text="5-Day Forecast",
            font=("Segoe UI", 22, "bold")
        )

        self.forecast_title.pack(
            pady=(20, 10)
        )

        self.forecast_frame = ctk.CTkFrame(
            self.right,
            fg_color="transparent"
        )

        self.forecast_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )
        self.button_frame = ctk.CTkFrame(
            self.right,
            fg_color="transparent"
        )

        self.button_frame.pack(
            pady=20
        )

        self.favorite_button = ctk.CTkButton(
            self.button_frame,
            text="⭐ Add Favorite",
            width=140,
            command=self.add_to_favorites
        )

        self.favorite_button.grid(
            row=0,
            column=0,
            padx=5
        )

        self.history_button = ctk.CTkButton(
            self.button_frame,
            text="📜 History",
            width=120,
            command=self.show_history
        )

        self.history_button.grid(
            row=0,
            column=1,
            padx=5
        )

        self.favorites_button = ctk.CTkButton(
            self.button_frame,
            text="❤️ Favorites",
            width=120,
            command=self.show_favorites
        )

        self.favorites_button.grid(
            row=0,
            column=2,
            padx=5
        )

        self.refresh_button = ctk.CTkButton(
            self.button_frame,
            text="🔄 Refresh",
            width=120,
            command=self.refresh_weather
        )

        self.refresh_button.grid(
            row=0,
            column=3,
            padx=5
        )

        self.theme_button = ctk.CTkButton(
            self.button_frame,
            text="🌙 Theme",
            width=120,
            command=self.toggle_theme
        )

        self.theme_button.grid(
            row=0,
            column=4,
            padx=5
        )

        self.after(
            1000,
            self.update_clock
        )

    # ==========================================================
    # LIVE CLOCK
    # ==========================================================

    def update_clock(self):

        self.time_label.configure(
            text=current_time()
        )

        self.after(
            1000,
            self.update_clock
        )

    # ==========================================================
    # SEARCH WEATHER
    # ==========================================================

    def search_weather(self):

        city = clean_city(
            self.city_entry.get()
        )

        if not valid_city(city):

            messagebox.showwarning(
                "Weather App",
                "Please enter a city name."
            )

            return

        weather, error = get_weather(city)

        if error:

            messagebox.showerror(
                "Weather App",
                error
            )

            return

        forecast, _ = get_forecast(city)

        self.current_weather = weather
        self.current_forecast = forecast or []

        save_history(city)

        self.update_weather()

    # ==========================================================
    # UPDATE WEATHER
    # ==========================================================

    def update_weather(self):

        weather = self.current_weather

        self.city_label.configure(
            text=f"{weather['city']}, {weather['country']}"
        )

        self.temp_label.configure(
            text=temperature(
                weather["temperature"]
            )
        )

        self.desc_label.configure(
            text=description(
                weather["description"]
            )
        )

        self.feels_label.configure(
            text=f"Feels Like {temperature(weather['feels_like'])}"
        )

        self.minmax_label.configure(
            text=f"Min {temperature(weather['temp_min'])}    Max {temperature(weather['temp_max'])}"
        )

        self.card_values["Humidity"].configure(
            text=humidity(
                weather["humidity"]
            )
        )

        self.card_values["Pressure"].configure(
            text=pressure(
                weather["pressure"]
            )
        )

        self.card_values["Wind"].configure(
            text=wind(
                weather["wind_speed"]
            )
        )

        self.card_values["Visibility"].configure(
            text=visibility(
                weather["visibility"]
            )
        )

        self.card_values["Sunrise"].configure(
            text=weather["sunrise"]
        )

        self.card_values["Sunset"].configure(
            text=weather["sunset"]
        )

        color = weather_color(
            weather["main"]
        )

        self.left.configure(
            fg_color=color
        )

        icon = load_icon(
            weather["main"]
        )

        if icon:

            self.icon_label.configure(
                image=icon,
                text=""
            )

            self.icon_label.image = icon

        self.update_forecast()
            # ==========================================================
    # UPDATE FORECAST
    # ==========================================================

    def update_forecast(self):

        for widget in self.forecast_frame.winfo_children():
            widget.destroy()

        if not self.current_forecast:
            return

        for day in self.current_forecast:

            card = ctk.CTkFrame(
                self.forecast_frame,
                width=120,
                height=170
            )

            card.pack(
                side="left",
                padx=8,
                pady=5,
                fill="y"
            )

            day_label = ctk.CTkLabel(
                card,
                text=day["day"],
                font=("Segoe UI", 16, "bold")
            )

            day_label.pack(
                pady=(10, 5)
            )

            icon = load_icon(
                day["main"]
            )

            if icon:

                icon_label = ctk.CTkLabel(
                    card,
                    image=icon,
                    text=""
                )

                icon_label.image = icon

                icon_label.pack(
                    pady=5
                )

            temp_label = ctk.CTkLabel(
                card,
                text=temperature(
                    day["temperature"]
                ),
                font=("Segoe UI", 18, "bold")
            )

            temp_label.pack()

            minmax = ctk.CTkLabel(
                card,
                text=f"{temperature(day['temp_min'])} / {temperature(day['temp_max'])}",
                font=("Segoe UI", 12)
            )

            minmax.pack(
                pady=(3, 3)
            )

            desc = ctk.CTkLabel(
                card,
                text=day["description"],
                wraplength=100,
                justify="center",
                font=("Segoe UI", 12)
            )

            desc.pack(
                padx=5,
                pady=(5, 10)
            )

    # ==========================================================
    # FAVORITES
    # ==========================================================

    def add_to_favorites(self):

        if not self.current_weather:

            messagebox.showwarning(
                "Weather App",
                "Search a city first."
            )

            return

        city = self.current_weather["city"]

        if add_favorite(city):

            messagebox.showinfo(
                "Favorites",
                f"{city} added to favorites."
            )

        else:

            messagebox.showinfo(
                "Favorites",
                f"{city} is already in favorites."
            )

    def show_favorites(self):

        favorites = get_favorites()

        window = ctk.CTkToplevel(self)

        window.title("Favorite Cities")

        window.geometry("350x450")

        title = ctk.CTkLabel(
            window,
            text="Favorite Cities",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(
            pady=15
        )

        textbox = ctk.CTkTextbox(
            window,
            width=300,
            height=320
        )

        textbox.pack(
            padx=20,
            pady=10
        )

        if favorites:

            for city in favorites:

                textbox.insert(
                    "end",
                    city + "\n"
                )

        else:

            textbox.insert(
                "end",
                "No favorite cities."
            )

        textbox.configure(
            state="disabled"
        )

    # ==========================================================
    # THEME
    # ==========================================================

    def toggle_theme(self):

        mode = ctk.get_appearance_mode()

        if mode == "Dark":

            ctk.set_appearance_mode(
                "Light"
            )

        else:

            ctk.set_appearance_mode(
                "Dark"
            )
                # ==========================================================
    # HISTORY
    # ==========================================================

    def show_history(self):

        history = get_history()

        window = ctk.CTkToplevel(self)

        window.title("Search History")

        window.geometry("450x500")

        title = ctk.CTkLabel(
            window,
            text="Search History",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(
            pady=15
        )

        textbox = ctk.CTkTextbox(
            window,
            width=380,
            height=350
        )

        textbox.pack(
            padx=20,
            pady=10
        )

        if history:

            for item in history:

                textbox.insert(
                    "end",
                    f"{item['city']}    ({item['time']})\n"
                )

        else:

            textbox.insert(
                "end",
                "No search history."
            )

        textbox.configure(
            state="disabled"
        )

        clear_button = ctk.CTkButton(
            window,
            text="Clear History",
            command=lambda: (
                clear_history(),
                window.destroy()
            )
        )

        clear_button.pack(
            pady=10
        )

    # ==========================================================
    # REFRESH WEATHER
    # ==========================================================

    def refresh_weather(self):

        if not self.current_weather:
            return

        city = self.current_weather["city"]

        self.city_entry.delete(
            0,
            "end"
        )

        self.city_entry.insert(
            0,
            city
        )

        self.search_weather()

    # ==========================================================
    # REMOVE CURRENT FAVORITE
    # ==========================================================

    def remove_current_favorite(self):

        if not self.current_weather:
            return

        city = self.current_weather["city"]

        if remove_favorite(city):

            messagebox.showinfo(
                "Favorites",
                f"{city} removed from favorites."
            )

        else:

            messagebox.showwarning(
                "Favorites",
                "City is not in favorites."
            )

    # ==========================================================
    # CLEAR SEARCH
    # ==========================================================

    def clear_search(self):

        self.city_entry.delete(
            0,
            "end"
        )

        self.current_weather = None
        self.current_forecast = []

        self.city_label.configure(
            text="Search a City"
        )

        self.temp_label.configure(
            text="--°C"
        )

        self.desc_label.configure(
            text=""
        )

        self.feels_label.configure(
            text="Feels Like --"
        )

        self.minmax_label.configure(
            text="Min --°C   Max --°C"
        )

        for value in self.card_values.values():

            value.configure(
                text="--"
            )

        self.icon_label.configure(
            image=None,
            text=""
        )

        for widget in self.forecast_frame.winfo_children():

            widget.destroy()

    # ==========================================================
    # ABOUT
    # ==========================================================

    def about(self):

        messagebox.showinfo(

            "Weather App Pro",

            "Weather App Pro\n\n"
            "Version 2.0\n\n"
            "Developed using:\n"
            "• Python\n"
            "• CustomTkinter\n"
            "• OpenWeather API\n"
            "• Pillow\n"
            "• Requests"

        )