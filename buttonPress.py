import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

while True:
	input_state = GPIO.input(4)
	if input_state == False:
		print('Button is pressed')
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(0.2)
	else:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)

GPIO.cleanup()
