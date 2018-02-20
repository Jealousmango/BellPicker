import RPi.GPIO as GPIO
import time
import random
import re
import json
from slackclient import SlackClient
import config

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
end = False
# Hold all GPIO pins used in a list.
contestants = [12, 18, 24, 25, 26, 27]

# Connect slack bot.
slack_client = SlackClient(config.api_key)

user_list = slack_client.api_call("users.list")

fantasticGifs = ["https://giphy.com/gifs/excited-the-office-celebrate-Is1O1TWV0LEJi",
				"https://giphy.com/gifs/news-atl-down-MTclfCr4tVgis",
				"https://giphy.com/gifs/cheer-cheering-oxW9IXKWP2Ouk",
				"https://giphy.com/gifs/studiosoriginals-domitille-collardey-l41Yh1olOKd1Tgbw4",
				"https://giphy.com/gifs/cat-reaction-youtubers-609o8uNjasiJO"]
# Used to ping winner.				
winnerNames = ["@lizl", "@charles.mitchell", "@shuggard", "@hubert-j-farnsworth", "@qwerji", "@eddrakee"]

for user in user_list.get("members"):
    if user.get("name") == "bellman":
        slack_user_id = user.get("id")
        break
if slack_client.rtm_connect():
    print ("Connected!")
    

def main():
	turnOffLeds()
	chooseWinner()
	
def turnOffLeds():
	GPIO.output(24, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(26, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)

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
	GPIO.output(winner, GPIO.HIGH)
	for blinks in range(0, 15):
		GPIO.output(winner, GPIO.LOW)
		time.sleep(.5)
		GPIO.output(winner, GPIO.HIGH)
	
	winningMessage = winnerHandle
	slack_client.api_call(
                    "chat.postMessage",
                    channel = "alert",
                    text = "The winner has been selected...",
                    as_user = True)
    
	time.sleep(1)
	
	slack_client.api_call(
                    "chat.postMessage",
                    channel = "alert",
                    text = winningMessage,
                    as_user = True,
                    link_names = True)
	fantasticGifToPost = random.randint(0, len(fantasticGifs) - 1)
	
	slack_client.api_call(
                    "chat.postMessage",
                    channel = "alert",
                    text = "You must answer the call of duty!",
                    as_user = True)
	
	slack_client.api_call(
                    "chat.postMessage",
                    channel = "alert",
                    text = fantasticGifs[fantasticGifToPost],
                    as_user = True)
# while end != True:	
while True:
	# Listen for button press.
	input_state = GPIO.input(4)
	if input_state == False:
		print("Button has been pressed.")
		main()
		print("5 second nap")
		time.sleep(15)
		# end = True
		# Shut it down.
		turnOffLeds()
		contestants = [12, 18, 24, 25, 26, 27]
	else:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)

# GPIO.cleanup()
print("Jobs done!")
