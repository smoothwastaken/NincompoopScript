import os, sys, time

# Colors and style part
import styles.main as style
from colorama import init, Fore, Back, Style
init(autoreset=True)
class Styling:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def show_art():
    print(style.home_art+"\n")

# Setup class
class Setup():
    def __init__(self):
        os.system("clear")
        show_art()
        print(f"Lauching the {Fore.LIGHTYELLOW_EX}{Styling.BOLD}setup{Fore.RESET}{Styling.END}!\n")
        time.sleep(1)

    def sudo_check(self):
        os.system('clear')
        show_art()
        for j in range(2):
            for i in range(4):
                os.system('clear')
                show_art()
                print(f"Checking if I have some sudo permissions" + "." * i)
                time.sleep(0.2)

        try:
            os.mkdir('/etc/foo')
            os.rmdir('/etc/foo')
        except PermissionError:
            sys.exit(f"{Fore.LIGHTRED_EX}{Styling.BOLD}❗️ - {Styling.UNDERLINE}Be sure that you launch this setup file with sudo permissions.")
        
        os.system("clear")
        show_art()
        print(f"{Fore.LIGHTGREEN_EX}✅ - SUDO PERMISSIONS ? Let's install!")
        time.sleep(2)

    def end(self):
        os.system("clear")
        show_art()
        sys.exit(f"{Styling.BOLD}{Fore.LIGHTBLUE_EX}Nincompoop Script{Styling.END}{Fore.LIGHTBLUE_EX} has been installed on your beautiful computer (don't make people mad with it thanks)")

if __name__ == "__main__":
    setup = Setup()
    setup.sudo_check()

    setup.end()