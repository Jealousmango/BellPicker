import RPi.GPIO as GPIO
import time
import random
from pad4pi import rpi_gpio

KEYPAD = [1, 2, 3, 4]

ROW_PINS = [21, 12, 25, 6, 5]
factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad = KEYPAD, row_pins = ROW_PINS)

def processKey(key):
	if (key == "1"):
		print("number")
	elif (key == "2"):
		print("number")
	elif (key == "3"):
		print("number")
	elif (key == "4"):
		print("number")
		
keypad.registerKeyPressHandler(processKey)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.IN)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

print ('How many loops: ')
GPIO.output(24, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)
x = input()
winnerIndex = 0

four = 0
eighteen = 0
twentyfour = 0
twentysix = 0
sixteen = 0
seventeen = 0
contestants = []

def main(four, eighteen, twentyfour, twentysix, sixteen, seventeen):
	
	GPIO.output(24, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(26, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(4, GPIO.LOW)
	GPIO.output(17, GPIO.LOW)
	
	#global winner
	#global four
	#global eighteen
	#global twentyfour
	#global twentysix
	#global sixteen


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
		global four
		global eighteen
		global twentyfour
		global twentysix
		global sixteen
		global seventeen
		
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
			print ('Lighting 16')
			GPIO.output(16, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(16, GPIO.LOW)
			time.sleep(.5)
			sixteen = sixteen + 1
		elif winner == 4:
			print ('Lighting 4')
			GPIO.output(4, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(4, GPIO.LOW)
			time.sleep(.5)
			four = four + 1
		else:
			print ('Lighting 17')
			GPIO.output(17, GPIO.HIGH)
			time.sleep(.5)
			GPIO.output(17, GPIO.LOW)
			time.sleep(.5)
			seventeen = seventeen + 1
			
		print ('Alerted')
		x = x - 1
	chooseWinner()

	while x != 0:
		chooseWinner()

main(four, eighteen, twentyfour, twentysix, sixteen, seventeen)

def displayWinner(four, eighteen, twentyfour, twentysix, sixteen, seventeen):
	print ('FOUR: ', four)
	print ('TWENTYSIX: ', twentysix)
	print ('SIXTEEN: ', sixteen)
	print ('EIGHTEEN: ', eighteen)
	print ('TWENTYFOUR: ', twentyfour)
	print ('SEVENTEEN: ', seventeen)
	print ('Thanks for playing!')

displayWinner(four, eighteen, twentyfour, twentysix, sixteen, seventeen)
keypad.cleanup()
GPIO.cleanup()



