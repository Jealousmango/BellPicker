import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def listenForPress():

    input_state = GPIO.input(4)
    if input_state == False:
        print("Button has been pressed.")
        sleep(.05)
        return False
    else:
        print("Button is not pressed.")
        sleep(.05)
        return True
