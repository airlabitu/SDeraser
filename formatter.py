# !/bin/python
# FormatterPi script 1.0
# Thomas Kaufmanas // AIRLAB // spring 2023

import time
import os

print("AIRLAB FormatterPi running...\n")
print("Reading volumes:")
os.system("lsblk")
time.sleep(1)
print("\n")

if input("Format volume /dev/sda? (y/n): ") == "y":
    print("Unmounting all partitions...")
    os.system("sudo umount /dev/sda?")
    time.sleep(0.5)
    print("Constructing partitioning table...")
    os.system("sudo parted -s -a optimal -- /dev/sda mklabel msdos")
    time.sleep(0.5)
    print("partitioning 100% of volume to fat32...")
    os.system("sudo parted -s -a optimal -- /dev/sda mkpart primary fat32 1MiB 100%")
    time.sleep(0.5)
    print("Cleaning up...")
    os.system("sudo parted -s -- /dev/sda align-check optimal 1")
    time.sleep(0.5)
    print("Formatting Volume...")
    os.system("sudo mkfs.vfat -F32 /dev/sda1")
    time.sleep(1)
    print("\nAll good - remove SD card")
else:
    print("quit")
    
