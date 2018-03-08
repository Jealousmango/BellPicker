import Led_Class
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Uncomment for home testing.
pin_12 = Led_Class.Led("ultraviolet", "@Jealousmango", 12)
pin_18 = Led_Class.Led("ultraviolet", "@Krysco", 18)
pin_24 = Led_Class.Led("ultraviolet", "@Jealousmango", 24)
pin_25 = Led_Class.Led("ultraviolet", "@Krysco", 25)
pin_26 = Led_Class.Led("ultraviolet", "@Jealousmango", 26)
pin_27 = Led_Class.Led("ultraviolet", "@Krysco", 27)

# Uncomment for work testing.
# pin_12 = Led_Class.Led("white", "@lizl", 12)
# pin_18 = Led_Class.Led("blue", "@charles.mitchell", 18)
# pin_24 = Led_Class.Led("green", "@shuggard", 24)
# pin_25 = Led_Class.Led("red", "@huber-j-farnsworth", 25)
# pin_26 = Led_Class.Led("orange", "@qwerji", 26)
# pin_27 = Led_Class.Led("pink", "@eddrakee", 27)

# Setup all GPIO pins.
pin_12.setup_led(pin_12.pin)
pin_18.setup_led(pin_18.pin)
pin_24.setup_led(pin_24.pin)
pin_25.setup_led(pin_25.pin)
pin_26.setup_led(pin_26.pin)
pin_27.setup_led(pin_27.pin)

contestants = [12, 18, 24, 25, 26, 27]

pin_12.turnOffLeds(pin_12.pin)
time.sleep(1)
pin_12.turnOnLeds(pin_12.pin)
time.sleep(1)
pin_12.turnOffLeds(pin_12.pin)
time.sleep(1)
pin_12.turnOnLeds(pin_12.pin)
time.sleep(1)
pin_12.turnOffLeds(pin_12.pin)
time.sleep(1)
pin_12.turnOnLeds(pin_12.pin)
time.sleep(1)

print(pin_12.color, pin_12.user_name, pin_12.pin)
print(pin_12)
