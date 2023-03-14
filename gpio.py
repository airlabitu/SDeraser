# !/bin/python
# GPIO script 1.0
# Thomas Kaufmanas // AIRLAB ITU // spring 2023

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

while True:
    GPIO.output(37, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(37, GPIO.LOW)
    time.sleep(0.1)