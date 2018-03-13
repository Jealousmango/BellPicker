import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Button(object):
    def __init__(self, pin=0):
            self.pin = pin
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def listenForButtonPress(self, pin):
        while True:
            # Listen for button press.
            input_state = GPIO.input(pin)
            if input_state == False:
                print("Button has been pressed.")
                return False
            else:
                return True


