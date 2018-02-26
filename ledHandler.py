import RPi.GPIO as GPIO
import buttonHandler

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)  # White
GPIO.setup(18, GPIO.OUT)  # Blue
GPIO.setup(24, GPIO.OUT)  # Green
GPIO.setup(25, GPIO.OUT)  # Red
GPIO.setup(26, GPIO.OUT)  # Orange
GPIO.setup(27, GPIO.OUT)  # Pink

def turnOffLeds():
    GPIO.output(24, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)

def turnOnLeds():
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)

