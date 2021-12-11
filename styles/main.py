from config import *

# Colors and style part
from colorama import init, Fore, Back, Style

init(autoreset=True)


class Styling:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


art = f"""{Fore.MAGENTA}{Styling.BOLD}<-. (`-')_   _      <-. (`-')_                       <-. (`-')   _  (`-')                        _  (`-') 
   \( OO) ) (_)        \( OO) ) _              .->      \(OO )_  \-.(OO )      .->        .->    \-.(OO ) 
,--./ ,--/  ,-(`-') ,--./ ,--/  \-,-----. (`-')----. ,--./  ,-.) _.'    \ (`-')----. (`-')----.  _.'    \ 
|   \ |  |  | ( OO) |   \ |  |   |  .--./ ( OO).-.  '|   `.'   |(_...--'' ( OO).-.  '( OO).-.  '(_...--'' 
|  . '|  |) |  |  ) |  . '|  |) /_) (`-') ( _) | |  ||  |'.'|  ||  |_.' | ( _) | |  |( _) | |  ||  |_.' | 
|  |\    | (|  |_/  |  |\    |  ||  |OO )  \|  |)|  ||  |   |  ||  .___.'  \|  |)|  | \|  |)|  ||  .___.' 
|  | \   |  |  |'-> |  | \   | (_'  '--'\\   '  '-'  '|  |   |  ||  |        '  '-'  '  '  '-'  '|  |      
`--'  `--'  `--'    `--'  `--'    `-----'    `-----' `--'   `--'`--'         `-----'    `-----' `--'      
                     (`-').->               (`-')    _       _  (`-') (`-')      
                     ( OO)_    _         <-.(OO )   (_)      \-.(OO ) ( OO).->   
                    (_)--\_)   \-,-----. ,------,)  ,-(`-')  _.'    \ /    '._   
                    /    _ /    |  .--./ |   /`. '  | ( OO) (_...--'' |'--...__) 
                    \_..`--.   /_) (`-') |  |_.' |  |  |  ) |  |_.' | `--.  .--' 
                    .-._)   \  ||  |OO ) |  .   .' (|  |_/  |  .___.'    |  |    
                    \       / (_'  '--'\ |  |\  \   |  |'-> |  |         |  |    
                     `-----'     `-----' `--' '--'  `--'    `--'         `--'    {Styling.END}
"""

credits = f"""
                {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}                   Nincompoop Script                    {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}
                {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}                        {config["version"]}                        {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}
                {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}          Author: {config["author"]}        {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}
                {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}                     License: {config["license"]}                      {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}

                {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}                    Twitter: {config["twitter"]}                   {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}
                {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}                   Instagram: {config["instagram"]}                  {Fore.LIGHTGREEN_EX}{Styling.BOLD}[----]{Styling.END}

Welcome here..
"""

home_art = f"""{art}\n                                      {credits}"""

