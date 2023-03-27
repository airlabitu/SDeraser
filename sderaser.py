# SDeraser live running script with button interaction (3.0).
# Searches for newly inserted volumes (blocks). Will attempt to delete the first block on list that starts with "sd..", following raspi block order ("sda, sdb, sdc.."" etc.).
# Uses a dual light push button as user interface. 
# Full documentation, and tutorial: https://github.com/airlabitu/SDeraser

# Thomas Kaufmanas // AIRLAB ITU // March 2023

import time
import os
import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
btnLED1 = 37
btnLED2 = 38
btn = 7
GPIO.setup(btnLED1,GPIO.OUT)
GPIO.setup(btnLED2,GPIO.OUT)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

waitstate = 1

# SD functions to interact with block
def blockCheck():
    """Use subprocess module to read block devices inserted. Returns a list of names"""
    output = subprocess.Popen("lsblk -l -o NAME", shell=True, stdout=subprocess.PIPE).stdout
    output = output.read()
    output = output.decode("utf-8")
    output = output.strip().split("\n")
    result = output[1:]
    #print("array er:", result)
    return result
def wipeSD(blockname):
    """formats an SD card by name of primary blocks (thereby including any partitions under this)"""
    b = blockname
    print("Unmounting all partitions...")
    os.system(f"sudo umount /dev/{b}?")
    time.sleep(0.5)
    print("Constructing partitioning table...")
    os.system(f"sudo parted -s -a optimal -- /dev/{b} mklabel msdos")
    time.sleep(0.5)
    print("partitioning 100% of volume to fat32...")
    os.system(f"sudo parted -s -a optimal -- /dev/{b} mkpart primary fat32 1MiB 100%")
    time.sleep(0.5)
    print("Cleaning up...")
    os.system(f"sudo parted -s -- /dev/{b} align-check optimal 1")
    time.sleep(0.5)
    print("Formatting Volume...")
    os.system(f"sudo mkfs.vfat -F32 /dev/{b}1")
    time.sleep(1)
    print("\nScript finished. Let's hope it worked. Remove SD card")
    for i in range(2): #Button animation 
        btnRed()
        time.sleep(0.2)
        btnOff()
        time.sleep(0.2)
        i =+ 1
    btnOff()
    return None

# Button functions to switch polarity and thereby colour of button
def btnRed():
	"""Sets button colour to red"""
	GPIO.output(btnLED1, GPIO.HIGH)
	GPIO.output(btnLED2, GPIO.LOW)
def btnGreen():
	"""Sets button colour to green"""
	GPIO.output(btnLED1, GPIO.LOW)
	GPIO.output(btnLED2, GPIO.HIGH)
def btnOff():
	"""Sets button colour to off"""
	GPIO.output(btnLED1, GPIO.LOW)
	GPIO.output(btnLED2, GPIO.LOW)

GPIO.cleanup
btnOff()
print("\nResetting GPIO's and buttons, launching SDeraser program...\n")
print("###############################################")

# Main loop
try:
    while True:
        blocks1 = blockCheck()
        time.sleep(2)
        blocks2 = blockCheck()
        if len(blocks2) > len(blocks1):  #Check if amount of volumes changes (aka. a block device is inserted)
            block = blocks2[0]
            print("CARD INSERTED. Contains the following:")
            os.system("lsblk")
            btnGreen()
            print(f"Format volume /dev/{block}? \n Press green button to continue")

            while not GPIO.input(btn): #Loop holds the code until button is pushed to confirm the erase
                time.sleep(0.1)

            for i in range(3): #Button animation 
                btnRed()
                time.sleep(0.1)
                btnOff()
                time.sleep(0.1)
                i =+ 1
            btnRed()

            if "sd" in block:   # Only erase block if it is named SD (as is expected)
                wipeSD(block)            
            elif "mmc" in block:    # Reject if it tries to erase itself
                print("Sorry, can't interact with my own block (MMCBLK)")
            else:
                print("Something went wrong - maybe the block isn't named 'sd...?' ")
            
        else:
            if waitstate == 1:  #Create an alternating wait messsage to make terminal look alive
                print("Waiting for SD....")
                waitstate = 0
            else:
                print("Waiting for SD..")
                waitstate = 1

            

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\n\n\n...Exit by user!\n")