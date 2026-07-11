import time
from colorama import Fore


def loading():

    print(Fore.CYAN + "\nFetching weather", end="")

    for _ in range(6):
        print(".", end="", flush=True)
        time.sleep(0.3)

    print("\n")