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

print ('How many loops: ')
GPIO.output(12, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)

x = input()
winnerIndex = 0

twentyfive = 0
eighteen = 0
twentyfour = 0
twentysix = 0
twelve = 0
twentyseven = 0
contestants = []

def turnOffLeds():
		GPIO.output(24, GPIO.LOW)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)


def main(twentyfive, eighteen, twentyfour, twentysix, twelve, twentyseven):
	
	#global winner
	#global four
	#global eighteen
	#global twentyfour
	#global twentysix
	#global sixteen
	
	turnOffLeds()
	
	def prepareWinner(winner):
		print("Hello")
		
	def chooseWinner():
		print('Winner winner, chicken dinner!')
		winner = random.randint(0, 5)
		# prepareWinner(winner)
		alertWinner(winner)

	def alertWinner(winner):
		global x
		#global winner
		global eighteen
		global twentyfour
		global twentysix
		global twelve
		global twentyfive
		global twentyseven
		
		print ('Alerting...')
		if winner == 0:
			print ('Lighting 18')
			GPIO.output(18, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(18, GPIO.LOW)
			time.sleep(.5)
			eighteen = eighteen + 1
		elif winner == 1:
			print ('Lighting 24')
			GPIO.output(24, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(24, GPIO.LOW)
			time.sleep(.5)
			twentyfour = twentyfour + 1
		elif winner == 2:
			print ('Lighting 26')
			GPIO.output(26, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(26, GPIO.LOW)
			time.sleep(.5)
			twentysix = twentysix + 1
		elif winner == 3:
			print ('Lighting 12')
			GPIO.output(12, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(12, GPIO.LOW)
			time.sleep(.5)
			twelve = twelve + 1
		elif winner == 4:
			print ('Lighting 25')
			GPIO.output(25, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(25, GPIO.LOW)
			time.sleep(.5)
			twentyfive = twentyfive + 1
		else:
			print ('Lighting 27')
			GPIO.output(27, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(27, GPIO.LOW)
			time.sleep(.5)
			twentyseven = twentyseven + 1
			
		print ('Alerted')
		x = x - 1
	chooseWinner()

	while x != 0:
		chooseWinner()

# main(twentyfive, eighteen, twentyfour, twentysix, twelve, twentyseven)

def displayWinner(four, eighteen, twentyfour, twentysix, twelve, seventeen):
	print ('TWENTYFIVE: ', twentyfive)
	print ('TWENTYSIX: ', twentysix)
	print ('TWELVE: ', twelve)
	print ('EIGHTEEN: ', eighteen)
	print ('TWENTYFOUR: ', twentyfour)
	print ('TWENTYSEVEN: ', twentyseven)
	print ('Thanks for playing!')

while x > 0:
	input_state = GPIO.input(4)
	if input_state == False:
		print('Button is pressed')
		#GPIO.output(12, GPIO.HIGH)
		#GPIO.output(18, GPIO.HIGH)
		#GPIO.output(24, GPIO.HIGH)
		#GPIO.output(25, GPIO.HIGH)
		#GPIO.output(26, GPIO.HIGH)
		#GPIO.output(27, GPIO.HIGH)
		#ime.sleep(0.2)
		main(twentyfive, eighteen, twentyfour, twentysix, twelve, twentyseven)
	else:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)

displayWinner(twentyfive, eighteen, twentyfour, twentysix, twelve, twentyseven)
turnOffLeds()
GPIO.cleanup()

