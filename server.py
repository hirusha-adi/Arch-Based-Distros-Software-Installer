import os
import sys
from datetime import datetime

print("[+] All imports completed successfully")


def clear():
    os.system("clear")


def install_program(package_name: str,
                    package_manager: str,
                    description: str,
                    logfile  # TextIOWrapper ?
                    ):
    yn = input(f"[?] Install - {package_name} ({description}):")
    if yn.lower().startswith("y"):
        os.system(f"{package_manager} -S {package_name}")
        logfile.write(
            f"{datetime.now()}: Installed {package_name} with {package_manager}\n")
    else:
        print(f"[-] Skipping {package_name}")
        logfile.write(f"{datetime.now()}: Not installing {package_name}\n")


clear()

# the log file
log = open(f"{os.getcwd()}/server.log", "w+", encoding="utf-8")
log.write(f"{datetime.now()}: Log file created, all imports were successfull\n")

os.system("pacman -S base-devel yay --noconfirm")
log.write(f"{datetime.now()}: Installed base-devel and yay with pacman\n")


clear()
print(r"""
 ____                           
/ ___|  ___ _ ____   _____ _ __ 
\___ \ / _ \ '__\ \ / / _ \ '__|
 ___) |  __/ |   \ V /  __/ |   
|____/ \___|_|    \_/ \___|_|   
""")


server_packages = (
    (
        "gnome-disk-utility",
        "pacman",
        "Manage Partitions+Automount fstab GUI"
    ),
    (
        # https://linuxhint.com/arch_linux_ssh_server/
        "openssh",
        "pacman",
        "for SSH Server"
    ),
    (
        "jellyfin",
        "yay",
        "Media Server"
    ),
    (
        "airsonic",
        "yay",
        "Music Server"
    ),
    (
        "filebrowser",
        "yay",
        "File Browsing Server"
    ),
    (
        "netdata",
        "yay",
        "Perfomance Monitor"
    ),
    (
        "qbittorrent",
        "pacman",
        "Torrent Client"
    )
)

for server_package_name, server_package_manager, server_package_description in server_packages:
    install_program(
        package_name=server_package_name,
        package_manager=server_package_manager,
        description=server_package_description,
        logfile=log
    )


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

# Jellyfin Server
print("[*] Setting up Jellyfin Server")
log.write(f"{datetime.now()}: Setting up Jellyfin Server\n")
os.system("systemctl start jellyfin")
log.write(f"{datetime.now()}: systemctl start jellyfin\n")
os.system("systemctl enbale jellyfin")
log.write(f"{datetime.now()}: systemctl enbale jellyfin\n")

# Airsonic Server
print("[*] Setting up Airsonic Server")
log.write(f"{datetime.now()}: Setting up Airsonic Server\n")
os.system("systemctl start airsonic")
log.write(f"{datetime.now()}: systemctl start airsonic\n")
os.system("systemctl enable airsonic")
log.write(f"{datetime.now()}: systemctl enable airsonic\n")

# Netdata Server
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

# Filebrowser Server
print("[*] Setting up FileBrowser Server")
log.write(f"{datetime.now()}: Setting up FileBrowser Server\n")
port = input("[?] Port (defaults to 8060): ")
if (port.strip()) == "":
    port = "8060"  # default port
log.write(f"{datetime.now()}: Selected port - {port}\n")
filepath = input("[?] File Path: ")
if (filepath.strip()) == "":
    filepath = "/mnt/"  # default root folder for server
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
