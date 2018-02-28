# import slackHandler as slackHandler
import buttonHandler as buttonHandler
import ledHandler as ledHandler
import sys
import time

# Prevent python from generating .pyc files.
sys.dont_write_bytecode = True

botMode = input('What mode? *default or testing')
test = 'test'

if botMode.lower() == test:
    print('Test mode.')
else:
    print('Default mode.')

    
def main():
    contestants = [12, 18, 24, 25, 26, 27]
    ledHandler.turnOffLeds()
    # TODO: change this to be called from user input.
    while True:
        buttonPressed = buttonHandler.listenForPress()
        if (buttonPressed):
            ledHandler.turnOnLeds()
        else:
            ledHandler.turnOffLeds()
main()    
