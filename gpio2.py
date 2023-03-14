from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # set GPIO to use the pin numbers instead of pin names

led_pin1 = 7 # pin number 7
led_pin2 = 11 # pin number 11

GPIO.setup(led_pin1,GPIO.OUT) # set the pin to output
GPIO.setup(led_pin2,GPIO.OUT) # set the pin to output

state = 0

try:
	print ("Look at the bicolor LED. It should be alternating. Ctrl+C to end.")
	while(1):
		GPIO.output(led_pin1,state)
		GPIO.output(led_pin2,not state)
		state = not state # reverse state
		sleep(.25) # wait a quarter second
except KeyboardInterrupt:
	GPIO.cleanup()