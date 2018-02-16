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

# GPIO.output(12, GPIO.HIGH)
# GPIO.output(18, GPIO.HIGH)
# GPIO.output(24, GPIO.HIGH)
# GPIO.output(25, GPIO.HIGH)
# GPIO.output(26, GPIO.HIGH)
# GPIO.output(27, GPIO.HIGH)
end = False
contestants =[12, 18, 24, 25, 26, 27]

def turnOffLeds():
		GPIO.output(24, GPIO.LOW)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)

def main():
	turnOffLeds()
	chooseWinner()

def chooseWinner():
	print('Winner winner, chicken dinner!')
	timeToWait = .5
	distanceToWinner = random.randint(0, len(contestants))
	for x in range(0, distanceToWinner):
		GPIO.output(contestants[x], GPIO.HIGH)
		time.sleep(timeToWait)
		if (x == distanceToWinner):
			winner = contestants[distanceToWinner]
			print("Winner is: ", winner)
			return(winner)
		else:
			timeToWait = timeToWait * 2
			GPIO.output(contestants[x], GPIO.LOW)
	
while end != True :
	input_state = GPIO.input(4)
	if input_state == False:
		print('Button is pressed')
		main()
		time.sleep(10)
		print("Napping for 10 seconds while winner is lit.")
		end = True
	else:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
# main()

GPIO.cleanup()
print("Jobs done!")


		# prepareWinner(winner)
		# Loop through array until distanceToWinner reaches zero, indicating the final winner.
		# while distanceToWinner > 0:
		# 	lightUpIndex(distanceToWinner, winner)
		# 	distanceToWinner = distanceToWinner - 1

		# GPIO.output(contestants[distanceToWinner], GPIO.HIGH)
		# alertWinner(winner)
	# 	print("Winner: ", contestants[displayWinner])

	# def lightUpIndex(distanceToWinner, winner):
	# 	timeToWait = .5
	# 	GPIO.output(contestants[distanceToWinner], GPIO.HIGH)
	# 	time.sleep(timeToWait)
	# 	GPIO.output(contestants[distanceToWinner], GPIO.LOW)
	# 	timeToWait = timeToWait * 2
	# 	return(distanceToWinner, winner)
	

	# def prepareWinner(winner):
		# Roll a random number to move away from selected index.
		# stepsFromIndex = random.randint(10, 20)
		# Loop through the array until stepsFromIndex is at 0
		
		

	# def alertWinner(winner):
	# 	global x
	# 	#global winner
	# 	global eighteen
	# 	global twentyfour
	# 	global twentysix
	# 	global twelve
	# 	global twentyfive
	# 	global twentyseven
		
	# 	print ('Alerting...')
	# 	if winner == 0:
	# 		print ('Lighting 18')
	# 		GPIO.output(18, GPIO.HIGH)
	# 		time.sleep(.5)
	# 		GPIO.output(18, GPIO.LOW)
	# 		time.sleep(.5)
	# 		eighteen = eighteen + 1
	# 	elif winner == 1:
	# 		print ('Lighting 24')
	# 		GPIO.output(24, GPIO.HIGH)
	# 		time.sleep(.5)
	# 		GPIO.output(24, GPIO.LOW)
	# 		time.sleep(.5)
	# 		twentyfour = twentyfour + 1
	# 	elif winner == 2:
	# 		print ('Lighting 26')
	# 		GPIO.output(26, GPIO.HIGH)
	# 		time.sleep(.5)
	# 		GPIO.output(26, GPIO.LOW)
	# 		time.sleep(.5)
	# 		twentysix = twentysix + 1
	# 	elif winner == 3:
	# 		print ('Lighting 12')
	# 		GPIO.output(12, GPIO.HIGH)
	# 		time.sleep(.5)
	# 		GPIO.output(12, GPIO.LOW)
	# 		time.sleep(.5)
	# 		twelve = twelve + 1
	# 	elif winner == 4:
	# 		print ('Lighting 25')
	# 		GPIO.output(25, GPIO.HIGH)
	# 		time.sleep(.5)
	# 		GPIO.output(25, GPIO.LOW)
	# 		time.sleep(.5)
	# 		twentyfive = twentyfive + 1
	# 	else:
	# 		print ('Lighting 27')
	# 		GPIO.output(27, GPIO.HIGH)
	# 		time.sleep(.5)
	# 		GPIO.output(27, GPIO.LOW)
	# 		time.sleep(.5)
	# 		twentyseven = twentyseven + 1
			
	# 	print ('Alerted')
	# 	x = x - 1
	# chooseWinner()

	# while x != 0:
	# 	chooseWinner()

# main(twentyfive, eighteen, twentyfour, twentysix, twelve, twentyseven)

# def displayWinner(four, eighteen, twentyfour, twentysix, twelve, seventeen):
# 	print ('TWENTYFIVE: ', twentyfive)
# 	print ('TWENTYSIX: ', twentysix)
# 	print ('TWELVE: ', twelve)
# 	print ('EIGHTEEN: ', eighteen)
# 	print ('TWENTYFOUR: ', twentyfour)
# 	print ('TWENTYSEVEN: ', twentyseven)
# 	print ('Thanks for playing!')

# while x > 0:
# 	input_state = GPIO.input(4)
# 	if input_state == False:
# 		print('Button is pressed')
# 		#GPIO.output(12, GPIO.HIGH)
# 		#GPIO.output(18, GPIO.HIGH)
# 		#GPIO.output(24, GPIO.HIGH)
# 		#GPIO.output(25, GPIO.HIGH)
# 		#GPIO.output(26, GPIO.HIGH)
# 		#GPIO.output(27, GPIO.HIGH)
# 		#ime.sleep(0.2)
# 		main(twentyfive, eighteen, twentyfour, twentysix, twelve, twentyseven)
# 	else:
# 		GPIO.output(18, GPIO.LOW)
# 		GPIO.output(26, GPIO.LOW)
# 		GPIO.output(24, GPIO.LOW)
# 		GPIO.output(12, GPIO.LOW)
# 		GPIO.output(27, GPIO.LOW)
# 		GPIO.output(25, GPIO.LOW)

# # displayWinner(twentyfive, eighteen, twentyfour, twentysix, twelve, twentyseven)
# turnOffLeds()
# GPIO.cleanup()

