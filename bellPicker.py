import json
import random
import re
import sys
import time

from gpiozero import Buzzer
from slackclient import SlackClient

import config
import RPi.GPIO as GPIO

buzzer = Buzzer(19)

# Prevent python from generating .pyc files.
sys.dont_write_bytecode = True

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(12, GPIO.OUT) # White
GPIO.setup(18, GPIO.OUT) # Blue
GPIO.setup(24, GPIO.OUT) # Green
GPIO.setup(25, GPIO.OUT) # Red
GPIO.setup(26, GPIO.OUT) # Orange
GPIO.setup(27, GPIO.OUT) # Pink

# Bool to let the program know when to end.
# end = False
# Hold all GPIO pins used in a list.
# contestants = [12, 18, 24, 25, 26, 27]

# mode = "demo"

def turnOffLeds():
    GPIO.output(24, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)

# Playing around with a demo mode.
# def demoMode():
#     turnOffLeds()
#     for i in range(0, len(contestants)):
#         GPIO.output(contestants[i], GPIO.HIGH)
#         print("Blinking!")
#         time.sleep(.5)
#         GPIO.output(contestants[i], GPIO.LOW)
#         time.sleep(.5)
#     demoMode()

# if mode == "demo":
#     demoMode()
# else:
#     print("No demo input.")


# Connect slack bot.
slack_client = SlackClient(config.api_key)
# slack_client = SlackClient(config.api_key_bottington)

user_list = slack_client.api_call("users.list")

fantasticGifs = ["https://giphy.com/gifs/excited-the-office-celebrate-Is1O1TWV0LEJi",
                "https://giphy.com/gifs/news-atl-down-MTclfCr4tVgis",
                "https://giphy.com/gifs/cheer-cheering-oxW9IXKWP2Ouk",
                "https://giphy.com/gifs/internet-eoxomXXVL2S0E",
                "https://giphy.com/gifs/cat-reaction-youtubers-609o8uNjasiJO",
                "https://giphy.com/gifs/reactionseditor-come-on-you-got-this-3og0IPMeREHpEV0f60",
                "https://giphy.com/gifs/heyarnold-nickelodeon-hey-arnold-26Ff4Ci2RNT1H1zb2"]
# Used to ping winner.
winnerNames = ["@lizl", "@charles.mitchell", "@shuggard", "@hubert-j-farnsworth", "@qwerji", "@eddrakee"]
# winnerNames = ["@jealousmango", "@krysco","@jealousmango", "@krysco","@jealousmango", "@krysco"]
contestants = [12, 18, 24, 25, 26, 27]
def main():
    contestants = [12, 18, 24, 25, 26, 27]
    turnOffLeds()
    chooseWinner()
    turnOffLeds()

def chooseWinner():
    print('Choosing winner...')
    # Amount of time to sleep between LEDs.
    timeToWait = .5
    # Capture the index that "wins"
    winningIndex = random.randint(0, len(contestants) - 1)
    winnerHandle = winnerNames[winningIndex]
    print("winningIndex is: ", winningIndex)
    # Save the value of the winning index and then remove it from the list.
    winner = contestants[winningIndex]
    contestants.remove(winner)
    # Loop through remaining "losers".
    for x in range(0, len(contestants)):
        # Light each losing pin.
        GPIO.output(contestants[x], GPIO.HIGH)
        print("Lighting index: ", contestants[x])
        time.sleep(timeToWait)
        # Turn off losing pin to prepare for the next pin to be lit.
        GPIO.output(contestants[x], GPIO.LOW)
        # Increase the amount of time to wait between pins.
        timeToWait = timeToWait * 1.25
    # Light up the winning pin.
    # GPIO.output(winner, GPIO.HIGH)
    for blinks in range(0, 10):
        GPIO.output(winner, GPIO.HIGH)
        print("Blinking!")
        time.sleep(1)
        GPIO.output(winner, GPIO.LOW)
        time.sleep(1)
    GPIO.output(winner, GPIO.HIGH)
    winningMessage = winnerHandle
    slack_client.api_call(
        "chat.postMessage",
        # channel = "general",
        channel = "alert",
        text = "The winner has been selected...",
        as_user = True)

    time.sleep(1)

    slack_client.api_call(
        "chat.postMessage",
        # channel = "general",
        channel = "alert",
        text = winningMessage,
        as_user = True,
        link_names = True)
    fantasticGifToPost = random.randint(0, len(fantasticGifs) - 1)

    slack_client.api_call(
        "chat.postMessage",
        # channel = "general",
        channel = "alert",
        text = "You have been chosen!",
        as_user = True)

    slack_client.api_call(
        "chat.postMessage",
        # channel = "general",
        channel = "alert",
        text = fantasticGifs[fantasticGifToPost],
        as_user = True)

for user in user_list.get("members"):
    if user.get("name") == "bellman":
        slack_user_id = user.get("id")
        break
if slack_client.rtm_connect():
    print ("Connected!")

    while True:
        # Listen for button press.
        input_state = GPIO.input(4)
        if input_state == False:
            print("Button has been pressed.")
            # buzzer.beep(on_time = .03, n = 3, background = False)
            main()
            print("Jobs done.")
            time.sleep(10)
            # end = True
            # Shut it down.
            turnOffLeds()
            # contestants = [12, 18, 24, 25, 26, 27]
        else:
            GPIO.output(18, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)

        for message in slack_client.rtm_read():
            if "text" in message and message["text"].startswith("<@%s>" % slack_user_id):
                print("Message received: %s" % json.dumps(message, indent=2))
                message_text = message['text']. \
                    split("<@%s>" % slack_user_id)[1]. \
                    strip()

                if re.match(r'.*(ding).*', message_text, re.IGNORECASE):
                    slack_client.api_call(
                        "chat.postMessage",
                        # channel = "general",
                        channel = "alert",
                        text="Selecting a winner...",
                        as_user=True)
                    main()
# while end != True:
# while True:
    # # Listen for button press.
    # input_state = GPIO.input(4)
    # if input_state == False:
    #     print("Button has been pressed.")
    #     main()
    #     print("Jobs done.")
    #     time.sleep(10)
    #     # end = True
    #     # Shut it down.
    #     turnOffLeds()
    #     contestants = [12, 18, 24, 25, 26, 27]
    # else:
    #     GPIO.output(18, GPIO.LOW)
    #     GPIO.output(26, GPIO.LOW)
    #     GPIO.output(24, GPIO.LOW)
    #     GPIO.output(12, GPIO.LOW)
    #     GPIO.output(27, GPIO.LOW)
    #     GPIO.output(25, GPIO.LOW)

# GPIO.cleanup()
