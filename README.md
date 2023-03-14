# SDeraser
SDeraser (formerly known as formatterpi) is an AIRLab Infrastructure that enables easy wiping of SD cards.
The build is based on a raspberry pi that runs a python script looking for SD cards, and wipes them upon user interaction.

## Contents
- Changelog.txt lists changes and preferences on the raspberry pi
- Formatter.py holds the initial scripting of wiping an SD card 
- Formatter2.py utilizes this script as a waiting loop to run in background
- gpio.py and gpio2.py contains testing codes for button work
- SDeraser.py holds the final script for the SDeraser station
