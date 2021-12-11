import os

from config import *

# Colors and style part
import styles.main as style
from colorama import init, Fore, Back, Style
init(autoreset=True)
class Styling:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def show_home_art():
    print(style.home_art, end="")

def show_menu():
    print(f"\n{Styling.UNDERLINE}Select your command and navigate among these:\n")
    for section in config["menu"]:
        print(f"    {Fore.LIGHTRED_EX}{Styling.BOLD}{Styling.UNDERLINE}{section}", end=" --> ")
        print(f"""{config["menu"][section]}\n""")

class Toolkit():
    def __init__(self):
        try:
            os.mkdir('/etc/foo')
            os.rmdir('/etc/foo')
            self.IS_SUDO = True
        except PermissionError:
            self.IS_SUDO = False

    def set_title(self, title):
        sys.stdout.write(f"\x1b]2;NincompoopScript - {title}\x07")

    def handle_cmd(self, cmd, title=f"Command output:", show_cmd=True):
        os.system("clear")
        if show_cmd:
            print(f"""The command --> {Fore.YELLOW}{Styling.UNDERLINE}{cmd}{Styling.END}\n{Fore.LIGHTYELLOW_EX}{Styling.BOLD}{title}""")
        else:
            print(f"""{Fore.LIGHTYELLOW_EX}{Styling.BOLD}{title}""")
        os.system(cmd)
        input(f"""\n\n{Fore.LIGHTBLUE_EX}{Styling.BOLD}Press ENTER to continue...""")

    def chosing(self):
        not_selected = True
        while not_selected:
            self.set_title(f"Menu")
            os.system("clear")
            show_home_art()
            if (self.IS_SUDO):
                print(f"{Styling.BOLD}{Fore.LIGHTGREEN_EX}[SUDO MODE]")
            else:
                print(f"{Styling.BOLD}{Fore.LIGHTRED_EX}[NORMAL MODE]")
            show_menu()
            cmd = str(input("--> #"))


            # Leave script
            if cmd.lower() in ["quit", "q", "exit", "leave", "goodbye"]:
                os.system("clear")
                sys.exit(f"{Fore.LIGHTRED_EX}Thank you a lot for using NincompoopScript!\nGoodluck, see you soon!")

            elif cmd.lower() in ["restart", "rs"]:
                os.system("python3 ./nincompoopscript.py")

            # ifconfig command
            elif cmd.lower() in ["ifconfig", "if"]:
                self.handle_cmd(cmd="ifconfig", title="Here's your ifconfig:", show_cmd=False)

            # get local ip
            elif cmd.lower() in ['ipl']:
                self.handle_cmd(cmd="""ifconfig en0 | awk '/inet /{print $2}'""", title="Here's your local IP address:")

            # get public ip
            elif cmd.lower() in ['ipp']:
                self.handle_cmd(cmd="""curl ifconfig.me""", title="Here's your local IP address:")

            # get mac address
            elif cmd.lower() in ["mac", "macaddress"]:
                self.handle_cmd(cmd="""ifconfig en0 | awk '/ether/{print $2}'""", title="Here's your MAC Address:")



if __name__ == "__main__":
    tk = Toolkit()
    tk.chosing()
