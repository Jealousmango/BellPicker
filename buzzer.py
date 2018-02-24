from gpiozero import Buzzer
from time import sleep
import RPi.GPIO as GPIO

buzzer = Buzzer(19)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while True:
	input_state = GPIO.input(4)
	if input_state == False:
		print("Button pressed")
		# buzzer.beep(on_time = .03, n = 3, background = False)
		buzzer.on()
		# sleep(.1)
		# buzzer.off()
	else:
		buzzer.off()
		# sleep(.1)
