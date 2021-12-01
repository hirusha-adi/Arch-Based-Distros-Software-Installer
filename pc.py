import os
from datetime import datetime

print("[+] All imports completed successfully")
def clear():
    os.system("clear")
clear()

LOG = ""
log = open(f"{os.getcwd()}/pc.log", "w+", encoding="utf-8")
log.write(f"{datetime.now()}: Log file created, all imports were successfull\n")

os.system("pacman -S base-devel --noconfirm")
log.write(f"{datetime.now()}: Installed base-devel with pacman\n")

os.system("pacman -S yay --noconfirm")
log.write(f"{datetime.now()}: Installed yay with pacman\n")


clear()
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

# bpytop (system monitor tool)
yn = input("[?] Install - bpytop (system monitor tool):")
if yn.lower().startswith("y"):
    os.system("pacman -S bpytop")
    log.write(f"{datetime.now()}: Installed bpytop with pacman\n")
else:
    print("[-] Skipping bpytop")
    log.write(f"{datetime.now()}: Not installing bpytop\n")

# htop (drop down terminal)
yn = input("[?] Install - htop (system monitor tool):")
if yn.lower().startswith("y"):
    os.system("pacman -S htop")
    log.write(f"{datetime.now()}: Installed htop with pacman\n")
else:
    print("[-] Skipping htop")
    log.write(f"{datetime.now()}: Not installing htop\n")

# flameshot (shreenshot utility)
yn = input("[?] Install - flameshot (shreenshot utility):")
if yn.lower().startswith("y"):
    os.system("pacman -S flameshot")
    log.write(f"{datetime.now()}: Installed flameshot with pacman\n")
else:
    print("[-] Skipping flameshot")
    log.write(f"{datetime.now()}: Not installing flameshot\n")

# spectacle (shreenshot utility)
yn = input("[?] Install - spectacle (shreenshot utility):")
if yn.lower().startswith("y"):
    os.system("pacman -S spectacle")
    log.write(f"{datetime.now()}: Installed spectacle with pacman\n")
else:
    print("[-] Skipping spectacle")
    log.write(f"{datetime.now()}: Not installing spectacle\n")

# woeusb (OS flashing tool)
yn = input("[?] Install - woeusb (OS flashing tool(For Windows)):")
if yn.lower().startswith("y"):
    os.system("pacman -S woeusb")
    log.write(f"{datetime.now()}: Installed woeusb with pacman\n")
else:
    print("[-] Skipping woeusb")
    log.write(f"{datetime.now()}: Not installing woeusb\n")

# etcher (OS flashing tool)
yn = input("[?] Install - etcher (OS flashing tool(Balena Etcher)):")
if yn.lower().startswith("y"):
    os.system("yay -S etcher")
    log.write(f"{datetime.now()}: Installed etcher with yay\n")
else:
    print("[-] Skipping etcher")
    log.write(f"{datetime.now()}: Not installing etcher\n")

clear()
print(r"""
 __  __          _ _       
|  \/  | ___  __| (_) __ _ 
| |\/| |/ _ \/ _` | |/ _` |
| |  | |  __/ (_| | | (_| |
|_|  |_|\___|\__,_|_|\__,_|
""")
# gimp (photo editor)
yn = input("[?] Install - gimp (shreenshot utility):")
if yn.lower().startswith("y"):
    os.system("pacman -S gimp")
    log.write(f"{datetime.now()}: Installed gimp with pacman\n")
else:
    print("[-] Skipping gimp")
    log.write(f"{datetime.now()}: Not installing gimp\n")

# jellyfin-media-player (Media Player for Jellyfin)
yn = input("[?] Install - jellyfin-media-player (shreenshot utility):")
if yn.lower().startswith("y"):
    os.system("yay -S jellyfin-media-player")
    log.write(f"{datetime.now()}: Installed jellyfin-media-player with pacman\n")
else:
    print("[-] Skipping jellyfin-media-player")
    log.write(f"{datetime.now()}: Not installing jellyfin-media-player\n")

# kdenlive (video editor)
yn = input("[?] Install - kdenlive (shreenshot utility):")
if yn.lower().startswith("y"):
    os.system("pacman -S kdenlive")
    log.write(f"{datetime.now()}: Installed kdenlive with pacman\n")
else:
    print("[-] Skipping kdenlive")
    log.write(f"{datetime.now()}: Not installing kdenlive\n")

# okular (PDF viewer for KDE)
yn = input("[?] Install - okular (PDF viewer for KDE):")
if yn.lower().startswith("y"):
    os.system("pacman -S okular")
    log.write(f"{datetime.now()}: Installed okular with pacman\n")
else:
    print("[-] Skipping okular")
    log.write(f"{datetime.now()}: Not installing okular\n")

# audacious (music player)
yn = input("[?] Install - audacious (music player):")
if yn.lower().startswith("y"):
    os.system("pacman -S audacious")
    log.write(f"{datetime.now()}: Installed audacious with pacman\n")
else:
    print("[-] Skipping audacious")
    log.write(f"{datetime.now()}: Not installing audacious\n")

# audacity (audio editor)
yn = input("[?] Install - audacity (audio editor):")
if yn.lower().startswith("y"):
    os.system("pacman -S audacity")
    log.write(f"{datetime.now()}: Installed audacity with pacman\n")
else:
    print("[-] Skipping audacity")
    log.write(f"{datetime.now()}: Not installing audacity\n")

# vlc (media player)
yn = input("[?] Install - vlc (media player):")
if yn.lower().startswith("y"):
    os.system("pacman -S vlc")
    log.write(f"{datetime.now()}: Installed vlc with pacman\n")
else:
    print("[-] Skipping vlc")
    log.write(f"{datetime.now()}: Not installing vlc\n")

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
yn = input("[?] Install - zoom (online meeting platform):")
if yn.lower().startswith("y"):
    os.system("yay -S zoom")
    log.write(f"{datetime.now()}: Installed zoom with yay\n")
else:
    print("[-] Skipping zoom")
    log.write(f"{datetime.now()}: Not installing zoom\n")

# teams (online meeting platform)
yn = input("[?] Install - teams (online meeting platform):")
if yn.lower().startswith("y"):
    os.system("yay -S teams")
    log.write(f"{datetime.now()}: Installed teams with yay\n")
else:
    print("[-] Skipping teams")
    log.write(f"{datetime.now()}: Not installing teams\n")


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
yn = input("[?] Install - vscodium (IDE (Open Source VS-Code)):")
if yn.lower().startswith("y"):
    os.system("yay -S vscodium")
    log.write(f"{datetime.now()}: Installed vscodium with yay\n")
else:
    print("[-] Skipping vscodium")
    log.write(f"{datetime.now()}: Not installing vscodium\n")

# pycharm-community-edition (IDE for Python)
yn = input("[?] Install - pycharm-community-edition (IDE for Python):")
if yn.lower().startswith("y"):
    os.system("yay -S pycharm-community-edition")
    log.write(f"{datetime.now()}: Installed pycharm-community-edition with yay\n")
else:
    print("[-] Skipping pycharm-community-edition")
    log.write(f"{datetime.now()}: Not installing pycharm-community-edition\n")

# sublime-text-4 (Text Editor))
yn = input("[?] Install - sublime-text-4 (Text Editor):")
if yn.lower().startswith("y"):
    os.system("yay -S sublime-text-4")
    log.write(f"{datetime.now()}: Installed sublime-text-4 with yay\n")
else:
    print("[-] Skipping sublime-text-4")
    log.write(f"{datetime.now()}: Not installing sublime-text-4\n")

# github-desktop (Management)
yn = input("[?] Install - github-desktop (Management):")
if yn.lower().startswith("y"):
    os.system("yay -S github-desktop")
    log.write(f"{datetime.now()}: Installed github-desktop with yay\n")
else:
    print("[-] Skipping github-desktop")
    log.write(f"{datetime.now()}: Not installing github-desktop\n")

log.write(f"{datetime.now()}: Installer completed. Have a nice day!")
log.close()
print("[+] Installer Completed\nHave a nice day!")
