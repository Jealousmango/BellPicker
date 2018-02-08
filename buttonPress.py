import RPi.GPIO as GPIO

# Configure pins so that the Pi knows that they are inputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(5 GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
print(GPIO.input(5))