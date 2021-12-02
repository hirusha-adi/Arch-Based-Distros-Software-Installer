import os
import sys
from datetime import datetime

print("[+] All imports completed successfully")
def clear():
    os.system("clear")
clear()

log = open(f"{os.getcwd()}/server.log", "w+", encoding="utf-8")
log.write(f"{datetime.now()}: Log file created, all imports were successfull\n")

os.system("pacman -S base-devel --noconfirm")
log.write(f"{datetime.now()}: Installed base-devel with pacman\n")

os.system("pacman -S yay --noconfirm")
log.write(f"{datetime.now()}: Installed yay with pacman\n")


clear()
print(r"""
 ____                           
/ ___|  ___ _ ____   _____ _ __ 
\___ \ / _ \ '__\ \ / / _ \ '__|
 ___) |  __/ |   \ V /  __/ |   
|____/ \___|_|    \_/ \___|_|   
            Install
""")

# gnome-disk-utility (Media Server)
yn = input("[?] Install - gnome-disk-utility (Manage Partitions+Automount fstab GUI):")
if yn.lower().startswith("y"):
    os.system("pacman -S gnome-disk-utility")
    log.write(f"{datetime.now()}: Installed gnome-disk-utility with pacman\n")
else:
    print("[-] Skipping gnome-disk-utility")
    log.write(f"{datetime.now()}: Not installing gnome-disk-utility\n")

# openssh (for SSH Server)
# https://linuxhint.com/arch_linux_ssh_server/
yn = input("[?] Install - openssh (for SSH Server):")
if yn.lower().startswith("y"):
    os.system("pacman -S openssh")
    log.write(f"{datetime.now()}: Installed openssh with yay\n")
else:
    print("[-] Skipping openssh")
    log.write(f"{datetime.now()}: Not installing openssh\n")

# jellyfin (Media Server)
yn = input("[?] Install - jellyfin (Media Server):")
if yn.lower().startswith("y"):
    os.system("yay -S jellyfin")
    log.write(f"{datetime.now()}: Installed jellyfin with yay\n")
else:
    print("[-] Skipping jellyfin")
    log.write(f"{datetime.now()}: Not installing jellyfin\n")

# airsonic (Music Server)
yn = input("[?] Install - airsonic (Music Server):")
if yn.lower().startswith("y"):
    os.system("yay -S airsonic")
    log.write(f"{datetime.now()}: Installed airsonic with yay\n")
else:
    print("[-] Skipping airsonic")
    log.write(f"{datetime.now()}: Not installing airsonic\n")

# filebrowser (File Server)
yn = input("[?] Install - filebrowser (Music Server):")
if yn.lower().startswith("y"):
    os.system("yay -S filebrowser")
    log.write(f"{datetime.now()}: Installed filebrowser with yay\n")
else:
    print("[-] Skipping filebrowser")
    log.write(f"{datetime.now()}: Not installing filebrowser\n")

# netdata (Perfomance Monitor)
yn = input("[?] Install - netdata (Perfomance Monitor):")
if yn.lower().startswith("y"):
    os.system("yay -S netdata")
    log.write(f"{datetime.now()}: Installed netdata with yay\n")
else:
    print("[-] Skipping netdata")
    log.write(f"{datetime.now()}: Not installing netdata\n")

# qbittorrent (Torrent Client)
yn = input("[?] Install - qbittorrent (Torrent Client):")
if yn.lower().startswith("y"):
    os.system("pacman -S qbittorrent")
    log.write(f"{datetime.now()}: Installed qbittorrent with pacman\n")
else:
    print("[-] Skipping qbittorrent")
    log.write(f"{datetime.now()}: Not installing qbittorrent\n")


log.write(f"{datetime.now()}: Installer completed")
print("[+] Installer Completed")

clear()
print(r"""
 ____       _               
/ ___|  ___| |_ _   _ _ __  
\___ \ / _ \ __| | | | '_ \ 
 ___) |  __/ |_| |_| | |_) |
|____/ \___|\__|\__,_| .__/ 
                     |_|    
""")

# Setup Automatically or Leave
yn = input("[?] Do you want to setup?[yes/n]: ")
if yn.lower().startswith("yes") == False:
    print("Have a nice day!")
    log.write(f"{datetime.now()}: Not setting up everything\n")
    log.write(f"{datetime.now()}: Have a nice day!")
    log.close()
    sys.exit()

# OpenSSH Server
print("[*] Setting up OpenSSH Server")
log.write(f"{datetime.now()}: Setting up OpenSSH Server\n")
os.system("systemctl start sshd")
log.write(f"{datetime.now()}: systemctl start sshd\n")
os.system("systemctl enable sshd")
log.write(f"{datetime.now()}: systemctl enable sshd\n")

# jellyfin Server
print("[*] Setting up Jellyfin Server")
log.write(f"{datetime.now()}: Setting up Jellyfin Server\n")
os.system("systemctl start jellyfin")
log.write(f"{datetime.now()}: systemctl start jellyfin\n")
os.system("systemctl enbale jellyfin")
log.write(f"{datetime.now()}: systemctl enbale jellyfin\n")

# airsonic Server
print("[*] Setting up Airsonic Server")
log.write(f"{datetime.now()}: Setting up Airsonic Server\n")
os.system("systemctl start airsonic")
log.write(f"{datetime.now()}: systemctl start airsonic\n")
os.system("systemctl enable airsonic")
log.write(f"{datetime.now()}: systemctl enable airsonic\n")

# netdata Server
print("[*] Setting up Netdata Server")
log.write(f"{datetime.now()}: Setting up Netdata Server\n")
os.system("systemctl start netdata")
log.write(f"{datetime.now()}: systemctl start netdata\n")
os.system("systemctl enable netdata")
log.write(f"{datetime.now()}: systemctl enable netdata\n")
os.system("ufw allow 19999/tcp")
log.write(f"{datetime.now()}: ufw allow 19999/tcp\n")
os.system("ufw reload")
log.write(f"{datetime.now()}: ufw reload\n")

# filebrowser Server
print("[*] Setting up FileBrowser Server")
log.write(f"{datetime.now()}: Setting up FileBrowser Server\n")
port = input("[?] Port (defaults to 8060): ")
if (port.strip()) == "":
    port = "8060" # default port
log.write(f"{datetime.now()}: Selected port - {port}\n")
filepath = input("[?] File Path: ")
if (filepath.strip()) == "":
    filepath = "/mnt/" # default root folder for server
log.write(f"{datetime.now()}: Selected root file path - {filepath}\n")
# fbr_cmnd = f"""#!/bin/bash\nfilebrowser -a "0.0.0.0" -p "{port}" -r "{filepath}" """
fbr_cmnd = f"""filebrowser -a "0.0.0.0" -p "{port}" -r "{filepath}" """
with open("startfilebrowser", "w", encoding="utf-8") as startfilebrowser:
    startfilebrowser.write(fbr_cmnd)
log.write(f"{datetime.now()}: Created file named - startfilebrowser\n")
os.system("chmod +x startfilebrowser")
log.write(f"{datetime.now()}: chmod +x startfilebrowser\n")
os.system("cp ./startfilebrowser /bin/startfilebrowser")
log.write(f"{datetime.now()}: cp ./startfilebrowser /bin/startfilebrowser\n")
print("[*] Enter 'startfilebrowser' in the terminal to start the server")

log.write(f"{datetime.now()}: Have a nice day!")
print("Have a nice day!")
log.close()
