####Made by Lymex
####Windows Version


import time
import os
os.system("pip install colorama")
os.system("pip install pythonping")
os.system("pip install python-whois")


from colorama import Fore
from pythonping import ping
import whois

os.system("cls")

print(Fore.MAGENTA + """

  __  __       _ _   _     _____           _ 
 |  \/  |_   _| | |_(_)   |_   _|__   ___ | |
 | |\/| | | | | | __| |_____| |/ _ \ / _ \| |
 | |  | | |_| | | |_| |_____| | (_) | (_) | |
 |_|  |_|\__,_|_|\__|_|     |_|\___/ \___/|_|
                                     by Lymex""")
print("")
time.sleep(5)
os.system("cls")


time.sleep(2)
print(Fore.GREEN + "25%.....")
time.sleep(2)
print(Fore.GREEN + "50%........")
time.sleep(2)
print(Fore.GREEN + "75%...........")
time.sleep(2)
print(Fore.GREEN + "100%..............")


os.system("cls")


print(Fore.BLUE + """
╔══════════════════════════════════════════════════╗
║ 1- inch to cm             2- cm to inch          ║
║                                                  ║
║ ═════════════════════════════════════════════════║
║ ═════════════════════════════════════════════════║
║ 3- ping                   4- whois               ║ 
║                                                  ║
╚══════════════════════════════════════════════════╝""")

while True:
    command = input(Fore.RED + "Command: ")
    if command == "1":
        inches = float(input('Enter inch: '))
        centi_meters = inches * 2.54
        centi_meters = round(centi_meters, 2)
        print(inches, 'Inches =', centi_meters, 'Centimeters')
    elif command == "2":
        centi = float(input('Enter centimeters: '))
        inch = centi * 0.39370079
        inch = round(inch, 2)
        print(centi, 'Centimeters', inch, 'Inches')
    elif command == "3":
        target = input("Enter IP: ")
        ping(target, verbose=True)
    elif command == "4":
        whotarget = input("Enter IP: ")
        whotext =whois.whois(whotarget)
        print(whotext)
