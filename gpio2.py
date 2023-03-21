# !/bin/python
# gpio2.py script to test GPIO in / out
# Introduces functions to change color on bi-color LED (inside button used)
# Thomas Kaufmanas // AIRLAB ITU // spring 2023

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
btnLED1 = 37
btnLED2 = 38
btn = 7

GPIO.setup(btnLED1,GPIO.OUT) # set the pin to output
GPIO.setup(btnLED2,GPIO.OUT) # set the pin to output
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


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


try:
	while True:
		btnRed()
		print("RED")
		time.sleep(0.5)

		btnGreen()
		print("GREEN")
		time.sleep(0.5)

		btnOff()
		print("OFF")
		time.sleep(0.5)

		print(GPIO.input(btn))

		GPIO.wait_for_edge(btn, GPIO.RISING)

except KeyboardInterrupt:
	GPIO.cleanup()