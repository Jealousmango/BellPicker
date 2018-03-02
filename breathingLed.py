import time
import RPi.GPIO as GPIO

LedPin = 18

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.LOW)

    p = GPIO.PWM(LedPin, 1000)
    p.start(0)

def loop():
    while True:
        for dc in range(0, 101, 4):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)
        for dc in range(100, -1, -4):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)

def destroy():
    p.stop()
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()


def destroy():
	p.stop()
	GPIO.output(LedPin, GPIO.HIGH)    # turn off all leds
	GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	except KeyboardInterrupt:
		destroy()
