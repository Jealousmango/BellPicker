import RPi.GPIO as GPIO
import time

# contestants = [12, 18, 24, 25, 26, 27]
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

print ('Let there be light.')
GPIO.output(12, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)

while True:
	input_state = GPIO.input(4)
	if input_state == False:
		print('Button is pressed')
		GPIO.output(12, GPIO.HIGH)
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		time.sleep(0.2)
	else:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)

GPIO.cleanup()
