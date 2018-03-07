import Led_Class
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin_12 = Led_Class.Led("ultraviolet", "@Jealousmango", 12)

pin_12.setup_led(pin_12.pin)
pin_12.turnOffLeds(pin_12.pin)
time.sleep(1)
pin_12.turnOnLeds(pin_12.pin)
time.sleep(1)

print(pin_12)
