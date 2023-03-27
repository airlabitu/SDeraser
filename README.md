# SDeraser
*SDeraser (formerly known as formatterpi) is an AIRLAB Infrastructure that enables easy formatting of SD cards. The core functionality consists of a python script that automatically detects newly inserted block devices (such as SD-cards or even USB drives), and subesequently erases the device using the ubuntu software "parted". For security reasons, it is important to note that the script is technically only formatting volumes (as opposed to wiping)!  The build is kept screenless and utilizes a button with a bicolor LED as user interaction via GPIO. A full tutorial for setup up can be found amongst [AIR LABs tutorials](https://airlab.itu.dk/category/tutorial/). Below is listed a quick Raspi Changelog of settings and configurations*

![alt text](https://airlab.itu.dk/wp-content/uploads/sites/71/2023/03/eraserpi.png)


## Contents
- Formatter2.py introduces the basic loop checking for an SD card, and erased upon terminal input = y.
- gpio2.py contains testing codes for working with bi-color LED and Button
- Launcher.sh holds the script used by LXDE-PI Autostart to launch SDeraser on boot
- SDeraser.py holds the final script for the SDeraser station

## Raspi Changelog

### Configurations
- (Optional) Changed Keyboard setup to danish
- removed automatic volume popup: filemanager > edit > preferences > volume management > uncheck "show available media types..."
- Enabled interfaces: Remote GPIO and VNC

### Terminal interactions
```sh
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install parted
```

```sh
# Github configuration (Optional)
$ sudo apt-get install git
$ mkdir gitcode
$ cd gitcode
$ git clone https://github.com/airlabitu/SDeraser.git
```

```sh
# Create launcher script, include contents from this directory:
$ sudo nano launcher.sh

# Make script executable:
$ chmod 755 launcher.sh
```

```sh
# Open the global autostart file and copy all lines to clipboard:
$ sudo nano /etc/xdg/lxsession/LXDE-pi/autostart

# Create user-side autostart script and paste all lines from the global one:
$ cd ~/.config/lxsession/LXDE-pi/
$ sudo nano autostart
# Additionally, add the following line to the autostart script, above "Xscreensaver":
@lxterminal -e "/home/pi/launcher.sh"
```
