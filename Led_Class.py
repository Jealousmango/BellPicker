import RPi.GPIO as GPIO

class Led(object):
    def __init__(self, color, user_name, pin=0):
        self.color = color
        self.pin = pin
        # Contains slack user name.
        self.user_name = user_name
    
    # Setup the pin passed.
    def setup_led(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    # Call this method output LOW on the pin passed.
    def turnOffLed(self, pin):
        GPIO.output(pin, GPIO.LOW)

    # Call this method output HIGH on the pin passed.
    def turnOnLed(self, pin):
        GPIO.output(pin, GPIO.HIGH)
