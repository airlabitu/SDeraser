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
	print ("Look at the bicolor LED. It should be alternating. Ctrl+C to end.")
	while(1):
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

except KeyboardInterrupt:
	GPIO.cleanup()