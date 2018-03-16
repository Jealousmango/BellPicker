import time
import RPi.GPIO as GPIO

# LedPin = 18

def setup():
    global twelve
    global eighteen
    global twentyFour
    global twentyFive
    global twentySix
    global twentySeven

    GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
#    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
#    GPIO.setup(27, GPIO.OUT)

    # GPIO.output(LedPin, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
#    GPIO.output(27, GPIO.LOW)
#    GPIO.output(25, GPIO.LOW)

    twelve = GPIO.PWM(12, 1000)
    eighteen = GPIO.PWM(18, 1000)
    twentyFour = GPIO.PWM(24, 1000)
#    twentyFive = GPIO.PWM(25, 1000)
    twentySix = GPIO.PWM(26, 1000)
#    twentySeven = GPIO.PWM(27, 1000)

    twelve.start(0)
    eighteen.start(0)
    twentyFour.start(0)
#    twentyFive.start(0)
    twentySix.start(0)
#    twentySeven.start(0)

def loop():
    while True:
        for dc in range(0, 101, 4):
            twelve.ChangeDutyCycle(dc)
            eighteen.ChangeDutyCycle(dc)
            twentyFour.ChangeDutyCycle(dc)
#            twentyFive.ChangeDutyCycle(dc)
            twentySix.ChangeDutyCycle(dc)
#            twentySeven.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)
        for dc in range(100, -1, -4):
            twelve.ChangeDutyCycle(dc)
            eighteen.ChangeDutyCycle(dc)
            twentyFour.ChangeDutyCycle(dc)
#            twentyFive.ChangeDutyCycle(dc)
            twentySix.ChangeDutyCycle(dc)
#            twentySeven.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)

def destroy():
    twelve.stop()
    eighteen.stop()
    twentyFour.stop()
#    twentyFive.stop()
    twentySix.stop()
#    twentySeven.stop()

    GPIO.output(12, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
#    GPIO.output(27, GPIO.HIGH)
#    GPIO.output(25, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	except KeyboardInterrupt:
		destroy()
