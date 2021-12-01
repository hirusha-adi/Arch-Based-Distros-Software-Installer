import os
import platform
import sys
import time
from datetime import datetime

print("[+] All imports completed successfully")
def clear():
    os.system("clear")
clear()

LOG = ""
log = open(f"{os.getcwd()}/pc.log", "w+", encoding="utf-8")
log.write(f"{datetime.now()}: Log file created, all imports were successfull\n")

os.system("pacman -S yay")
log.write(f"{datetime.now()}: Installed yay with pacman\n")

# base-devel (required for building packages)
# please install this, especially for manjaro
# yay wont be able to enter a fakeroot enviroment when installing packages
yn = input("[?] Install - base-devel (required for building packages):")
if yn.lower().startswith("y"):
    os.system("pacman -S base-devel")
    log.write(f"{datetime.now()}: Installed base-devel with pacman\n")
else:
    print("[-] Skipping base-devel")
    log.write(f"{datetime.now()}: Not installing base-devel\n")

print(r"""
 _   _ _   _ _ _ _   _           
| | | | |_(_) (_) |_(_) ___  ___ 
| | | | __| | | | __| |/ _ \/ __|
| |_| | |_| | | | |_| |  __/\__ \
 \___/ \__|_|_|_|\__|_|\___||___/
""")

# yakuake (drop down terminal)
yn = input("[?] Install - yakuake (Drop down terminal):")
if yn.lower().startswith("y"):
    os.system("pacman -S yakuake")
    log.write(f"{datetime.now()}: Installed yakuake with pacman\n")
else:
    print("[-] Skipping yakuake")
    log.write(f"{datetime.now()}: Not installing yakuake\n")

clear()
print(r"""
 __  __           _   _             
|  \/  | ___  ___| |_(_)_ __   __ _ 
| |\/| |/ _ \/ _ \ __| | '_ \ / _` |
| |  | |  __/  __/ |_| | | | | (_| |
|_|  |_|\___|\___|\__|_|_| |_|\__, |
                              |___/ 
""")

# zoom (online meeting platform)
yn = input("[?] Install - yakuake (online meeting platform):")
if yn.lower().startswith("y"):
    os.system("yay -S zoom")
    log.write(f"{datetime.now()}: Installed yakuake with yay\n")
else:
    print("[-] Skipping zoom")
    log.write(f"{datetime.now()}: Not installing yakuake\n")


clear()
print(r"""
 __  __                           _             
|  \/  | ___  ___ ___  __ _  __ _(_)_ __   __ _ 
| |\/| |/ _ \/ __/ __|/ _` |/ _` | | '_ \ / _` |
| |  | |  __/\__ \__ \ (_| | (_| | | | | | (_| |
|_|  |_|\___||___/___/\__,_|\__, |_|_| |_|\__, |
                            |___/         |___/ 
""")

# discord (messaging app)
yn = input("[?] Install - discord (messaging app):")
if yn.lower().startswith("y"):
    os.system("pacman -S discord")
    log.write(f"{datetime.now()}: Installed discord with pacman\n")
else:
    print("[-] Skipping discord")
    log.write(f"{datetime.now()}: Not installing discord\n")

# telegram-desktop (messaging app)
yn = input("[?] Install - telegram-desktop (messaging app):")
if yn.lower().startswith("y"):
    os.system("pacman -S telegram-desktop")
    log.write(f"{datetime.now()}: Installed telegram-desktop with pacman\n")
else:
    print("[-] Skipping telegram-desktop")
    log.write(f"{datetime.now()}: Not installing telegram-desktop\n")

# whatsapp-for-linux (messaging app)
yn = input("[?] Install - whatsapp-for-linux (messaging app):")
if yn.lower().startswith("y"):
    os.system("yay -S whatsapp-for-linux")
    log.write(f"{datetime.now()}: Installed whatsapp-for-linux with yay\n")
else:
    print("[-] Skipping whatsapp-for-linux")
    log.write(f"{datetime.now()}: Not installing whatsapp-for-linux\n")

# signal-desktop (messaging app)
yn = input("[?] Install - signal-desktop (messaging app):")
if yn.lower().startswith("y"):
    os.system("pacman -S signal-desktop")
    log.write(f"{datetime.now()}: Installed signal-desktop with pacman\n")
else:
    print("[-] Skipping signal-desktop")
    log.write(f"{datetime.now()}: Not installing signal-desktop\n")
    
clear()
print(r"""
 ____                 _                                  _   
|  _ \  _____   _____| | ___  _ __  _ __ ___   ___ _ __ | |_ 
| | | |/ _ \ \ / / _ \ |/ _ \| '_ \| '_ ` _ \ / _ \ '_ \| __|
| |_| |  __/\ V /  __/ | (_) | |_) | | | | | |  __/ | | | |_ 
|____/ \___| \_/ \___|_|\___/| .__/|_| |_| |_|\___|_| |_|\__|
                             |_|                             
""")

# eclipse-java (IDE for Java)
yn = input("[?] Install - eclipse-java (IDE for Java):")
if yn.lower().startswith("y"):
    os.system("yay -S eclipse-java")
    log.write(f"{datetime.now()}: Installed eclipse-java with yay\n")
else:
    print("[-] Skipping eclipse-java")
    log.write(f"{datetime.now()}: Not installing eclipse-java\n")

# visual-studio-code-bin (IDE)
yn = input("[?] Install - visual-studio-code-bin (IDE for Java):")
if yn.lower().startswith("y"):
    os.system("yay -S visual-studio-code-bin")
    log.write(f"{datetime.now()}: Installed visual-studio-code-bin with yay\n")
else:
    print("[-] Skipping visual-studio-code-bin")
    log.write(f"{datetime.now()}: Not installing visual-studio-code-bin\n")

# vscodium (IDE (Open Source VS-Code))
yn = input("[?] Install - vscodium (IDE for Java):")
if yn.lower().startswith("y"):
    os.system("yay -S vscodium")
    log.write(f"{datetime.now()}: Installed vscodium with yay\n")
else:
    print("[-] Skipping vscodium")
    log.write(f"{datetime.now()}: Not installing vscodium\n")

# pycharm-community-edition (IDE for Python)
yn = input("[?] Install - pycharm-community-edition (IDE for Java):")
if yn.lower().startswith("y"):
    os.system("yay -S pycharm-community-edition")
    log.write(f"{datetime.now()}: Installed pycharm-community-edition with yay\n")
else:
    print("[-] Skipping pycharm-community-edition")
    log.write(f"{datetime.now()}: Not installing pycharm-community-edition\n")



