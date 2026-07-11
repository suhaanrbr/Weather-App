"""
gui.py
Main GUI Window
"""

import customtkinter as ctk

from dashboard import Dashboard
from config import (
    APP_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MIN_WIDTH,
    MIN_HEIGHT,
    DEFAULT_APPEARANCE,
    DEFAULT_THEME
)


class WeatherApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        ctk.set_appearance_mode(
            DEFAULT_APPEARANCE
        )

        ctk.set_default_color_theme(
            DEFAULT_THEME
        )

        self.title(APP_TITLE)

        self.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.minsize(
            MIN_WIDTH,
            MIN_HEIGHT
        )

        self.dashboard = Dashboard(self)

        self.dashboard.pack(
            fill="both",
            expand=True
        )


def start_gui():

    app = WeatherApp()

    app.mainloop()