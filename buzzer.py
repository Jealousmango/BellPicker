from gpiozero import Buzzer
from time import sleep
import RPi.GPIO as GPIO

buzzer = Buzzer(19)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


while True:
	input_state = GPIO.input(4)
	if input_state == False:
		print("Button pressed")
		# buzzer.beep(on_time = .03, n = 3, background = False)
		buzzer.on()
		# sleep(.1)
		# buzzer.off()
		'''
		GPIO.output(12, GPIO.HIGH)
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		'''
	else:
		buzzer.off()
		'''
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
		# sleep(.1)
		'''
