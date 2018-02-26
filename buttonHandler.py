import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def listenForPress():

    input_state = GPIO.input(4)
    if input_state == False:
        print("Button has been pressed.")