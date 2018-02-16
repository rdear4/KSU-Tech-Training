
import random
import time

import RPi.GPIO as GPIO

# Set the board pin reference mode
# There are two options here. GPIO.BOARD which referes to the swquencial pin numbers 
# as they appear in order on the board and GPIO.BCM which refers to the pin name on
# the chip. e.g. GPIO17
GPIO.setmode(GPIO.BCM)

# Define the pin for the button
buttonPin = 12

# Define array of answers, in the form of tuples, and pin numbers
answers = [
	
	('Affirmative', 24),
	('Let me sleep on it. I\'ll give you an answer in the morning', 18),
	('Negative, Ghost Rider', 23),


]

# This loops through all the answer and set the pins for the corresponding LEDS
# to an output mode so that we can use them later
def setupPins():

	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	for answer in answers:
	
		pinNumber = answer[1]
		
		GPIO.setup(pinNUmber, GPIO.OUT)

		GPIO.output(pinNumber, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(pinNumber, GPIO.LOW)


def shake():
	print('Shaking')	
	# Get a random number between 0 and the number of answers in the array
	randomAnswerNumber = random.randint(0, len(answers) - 1)
	
	randomAnswer = answers[randomAnswerNumber]
	
	animateTo(randomAnswer[1])
	
def animateTo(answerNumber):
	
	blinksUntilAnswer = 20		#number of LEDs that will blink before giving us our answer
	delayBetweenLEDs = 0.25		#delay of 1/4 of a second
	
	for n in range(0, 20):
		
		turnLEDsOff()
		
		randomAnswerNumber = random.randint(0, len(answers) - 1)
		
		randomAnswer = answers[randomAnswerNumber]
		
		randomAnswerPin = randomAnswer[1]
		
		GPIO.output(randomAnswerPin, GPIO.HIGH)
		print(randomAnswer[0])
		time.sleep(delayBetweenLEDs)

	turnLEDsOff()
# 	
	GPIO.output(answerNumber, GPIO.HIGH)

def turnLEDsOff():
	
	for answer in answers:
	
		pinNumber = answer[1]
		
		GPIO.output(pinNumber, GPIO.LOW)

if __name__ == '__main__':
	
	# Setup the pins so we can use them to turn on the LEDs
	setupPins()
	
	loop = True
	# Once the program is run it will loop forever
	while loop:
			
		buttonState = GPIO.input(buttonPin)
			
		# Check to see if the button was being pressed
		if !buttonIsBeingPressed:
			
			# Check to see if the button has been pressed
			
	# 		buttonState = False		
			if buttonState == False:
				
				buttonIsBeingPressed = True
				# Start the process 'shake' the ball
				shake()
				loop = False
				
		else:
		
			if buttonState == True:
			
				buttonIsBeingPressed = False