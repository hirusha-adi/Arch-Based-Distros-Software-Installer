# Arch-Based-Distros-Software-Installer

For both my pc and my server

# PC

Required -

- yay
- base-devel

Utilities -

- yakuake (Drop down terminal)
- bpytop (system monitor tool)
- htop (system monitor tool)
- flameshot (shreenshot utility)
- spectacle (shreenshot utility)
- woeusb (OS flashing tool)
- etcher (OS flashing tool)

Media -

- gimp (photo editor)
- jellyfin-media-player (Media Player for Jellyfin)
- kdenlive (video editor)
- okular (PDF viewer for KDE)
- audacious (music player)
- audacity (audio editor)
- vlc (media player)

Meeting -

- zoom (online meeting platform)
- teams (online meeting platform)

Messaging -

- discord (messaging app)
- telegram-desktop (messaging app)
- whatsapp-for-linux (messaging app)
- signal-desktop (messaging app)

Development -

- eclipse-java (IDE for Java)
- visual-studio-code-bin (IDE)
- vscodium (IDE (Open Source VS-Code))
- pycharm-community-edition (IDE for Python)
- sublime-text-4 (Text Editor))
- github-desktop (Management)

The log file (`pc.log`) will be saved the current working directory

# Server

Installs -

- gnome-disk-utility (Manage Partitions+Automount fstab GUI)
- openssh (for SSH Server)
- jellyfin (Media Server)
- airsonic (Music Server)
- filebrowser (File Server)
- netdata (Perfomance Monitor)
- qbittorrent (Torrent Client)

Setup -

- OpenSSH Server

```bash
systemctl start sshd
systemctl enable sshd
```

- Jellyfin Server

```bash
systemctl start jellyfin
systemctl enable jellyfin
```

- Airsonic Server

```bash
systemctl start airsonic
systemctl enable airsonic
```

- Netdata Server

```bash
systemctl start netdata
systemctl enable netdata
ufw allow 19999/tcp
ufw reload
```

- Filebrowser Server

```bash
echo 'filebrowser -a "0.0.0.0" -p "0.0.0.0" -r "8060" ' >> startfilebrowser
chmod +x startfilebrowser
cp ./startfilebrowser /bin/startfilebrowser
# run startfilebrowser in the terminal
```
