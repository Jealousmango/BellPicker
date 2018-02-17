import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
# Bool to let the program know when to end.
end = False
# Hold all GPIO pins used in a list.
contestants =[12, 18, 24, 25, 26, 27]

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
		timeToWait = timeToWait * 1.3
	# Light up the winning pin.
	GPIO.output(winner, GPIO.HIGH)
	print("Winner is: ", winner)
	
while end != True :
	# Listen for button press.
	input_state = GPIO.input(4)
	if input_state == False:
		print("Button has been pressed.")
		main()
		print("5 second nap")
		time.sleep(5)
		end = True
		# Shut it down.
		turnOffLeds()
	else:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)

# GPIO.cleanup()
print("Jobs done!")
