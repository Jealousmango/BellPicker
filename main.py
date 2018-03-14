import Led_Class
import Button_Class
import SlackBot_Class
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

contestants = [pin_12, pin_18, pin_24, pin_25, pin_26, pin_27]

bottington = SlackBot_Class.SlackBot("bottington")
# bellman = SlackBot_Class.SlackBot("bellman")

# contestants = [12, 18, 24, 25, 26, 27]

def main():
    announce_bot = "Connected SlackBot: ", bottington.bot_name
    print("Running")

    bottington.send_message(announce_bot, "general")
    # contestants = [pin_12, pin_18, pin_24, pin_25, pin_26, pin_27]
    button = Button_Class.Button(4)
    bottington.connect_to_slack(bottington.bot_name)

    # bellman.connect_to_slack(bellman.bot_name)
    while button.listenForButtonPress(4) == True:
        turn_off_all_leds()
    else:
        print("Let there be light!")
        turn_on_all_leds()
        time.sleep(.1)
        main()

        # turn_off_all_leds()
        # time.sleep(1)
        # turn_on_all_leds()
        # time.sleep(1)
        # turn_off_all_leds()
        # time.sleep(1)
        # turn_on_all_leds()
        # time.sleep(1)
        # turn_off_all_leds()

def turn_off_all_leds():
    for x in range(0, len(contestants)):
        contestants[x].turnOffLed(contestants[x].pin)
    


def turn_on_all_leds():
    for x in range(0, len(contestants)):
        contestants[x].turnOnLed(contestants[x].pin)
    print("All LEDs turned on!")

# pin_12.turnOffLed(pin_12.pin)
# time.sleep(1)
# pin_12.turnOnLed(pin_12.pin)
# time.sleep(1)
# pin_12.turnOffLed(pin_12.pin)
# time.sleep(1)
# pin_12.turnOnLed(pin_12.pin)
# time.sleep(1)
# pin_12.turnOffLed(pin_12.pin)
# time.sleep(1)
# pin_12.turnOnLed(pin_12.pin)
# time.sleep(1)

main()
print(pin_12.color, pin_12.user_name, pin_12.pin)
print(pin_12)
