"""
loading.py
Loading screen widget for Weather App Pro
"""

import customtkinter as ctk


class LoadingFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(
            fg_color="transparent"
        )

        self.label = ctk.CTkLabel(
            self,
            text="Fetching Weather...",
            font=("Segoe UI", 22, "bold")
        )

        self.label.pack(
            pady=(30, 10)
        )

        self.progress = ctk.CTkProgressBar(
            self,
            width=350
        )

        self.progress.pack(
            pady=10
        )

        self.progress.set(0)

        self.running = False

    # ==========================================
    # START
    # ==========================================

    def start(self):

        self.running = True

        self.progress.start()

        self.animate()

    # ==========================================
    # STOP
    # ==========================================

    def stop(self):

        self.running = False

        self.progress.stop()

        self.progress.set(0)

        self.label.configure(
            text="Fetching Weather..."
        )

    # ==========================================
    # ANIMATION
    # ==========================================

    def animate(self):

        if not self.running:
            return

        text = self.label.cget("text")

        if text.endswith("..."):
            text = "Fetching Weather"

        else:
            text += "."

        self.label.configure(
            text=text
        )

        self.after(
            400,
            self.animate
        )


# ==========================================
# SMALL POPUP LOADER
# ==========================================

class LoadingPopup(ctk.CTkToplevel):

    def __init__(self, master):

        super().__init__(master)

        self.title("Loading")

        self.geometry("320x120")

        self.resizable(False, False)

        self.attributes("-topmost", True)

        self.loading = LoadingFrame(self)

        self.loading.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.loading.start()

    def close(self):

        self.loading.stop()

        self.destroy()


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    app = ctk.CTk()

    app.geometry("500x300")

    loader = LoadingFrame(app)

    loader.pack(expand=True)

    loader.start()

    app.mainloop()