###################################################################
#
#	Title 		: Python Basics
#	Author		: Ron Dear
#	Date		: 9/12/2017
#	Description	: In this script we will go through the basics of
#				  the python programming language		
#
###################################################################

# Include any external libraries to be used later, at the top of your code

import random	# We will use the random library later to generate a random number


# This is a comment. In many other programming languages comments are denoted using
# two '/' for a single line comment or a '/*' followed by the text of the comment
# and ending with a '*/' for multi-line comments. 

# In Python single line comments are denoted by a hashtag symbol. 

# Print statements

print("This is how you print something to the screen")

# Every print statement show up on its own line.

print("See!?")

# print statements can be super helpful when trying to figure out where your program
# went wrong or when trying to get information to your user.

# User input

# To get input from your user, simply use the raw_input function like so:

usersName = raw_input("What is your name? ")

# The 'usersName' is the name of the variable you will use to store the name of the user

# Variables

# With python you do not need to tell the the program what kind of data you want to
# store in the variable. You just give the varaible a name and some data.

myAge = 33						# Integer
myName = "Ron Dear"				# String
myFavTemp = 70.3				# Float
likesProgramming = True			# Boolean

# These are some of the basic Python data types.

# In the 'raw_input' example above we stored the user's input, ideally their name, in 
# the variable named 'usersName'. Let's print that out to the screen now

print(usersName)

# We can also print some of our own text to add some context to it.

print("The user's name is : " + usersName)

# Let's write a simple program that adds two numbers.
# The first thing we have to do is get some numbers from the user

firstNumber = raw_input("First number : ")
secondNumber = raw_input("Second number : ")

total = firstNumber + secondNumber

print("The total of the two number is : " + total)

# That didn't quite work out the way we thought. The reason for that is the
# program didn't add the two numbers together using math, they just pushed them
# together like we were concatenating a string.

# To get our program to do math we need to tell it that the numbers are numbers and
# and not just text.

# To do that we 'cast' them as integers like this

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

total = firstNumber + secondNumber

# print("Now the total of the two number is : " + total)

# Now we're getting an error becauase now we have the opposite problem.
# The print statement will only print out strings and now the 'total' variable is a
# number. We need to cast it as a string to print it out

print("Now the total of the two number is : " + str(total))

#There's some basic math, now let's talk about control structures

# If statements

print(" ")

currentTemperature = 64.2

if (currentTemperature > myFavTemp):
	
	print("It's too warm in here")
	
else:

	print("It's too cold in here")
	
# If the statement inside the parenthesis is true, then the code under the first
# first line of the if statement is evaluated.

# If the statement is false, then the code in the else section is evaluated.

complaint = ""

if (currentTemperature > myFavTemp):

	complaint = "warm"
	
else:
	
	complaint = "cold"
	
print("It's too " + complaint + " in here")

if (currentTemperature > myFavTemp):

	if (currentTemperature > myFavTemp + 20):
		
		print("IT'S WAY TOO HOT IN HERE!")
	
	else:	
		
		print("It's too warm in here")

else:
	
	if (currentTemperature < myFavTemp - 20):
		
		print("IT'S FREEZING IN HERE!")
	
	else:	
		
		print("It's too cool in here")
	
# Evaluating If statements with strings

print(" ")

if (usersName == "Ron"):
	
	print("Hello, Ron")
	
else:

	print("Unknown user. Security has been alerted")
	
	
# Loops

# For Loop

# The code in this loop will execute a given number of times for
# numbers from the begining of the range to end minus 1

print(" ")

for i in range(0, 12):
	
	print("The current number in the loop is " + str(i))
	
print("")

for j in range(0, 10):

	square = j * j
	
	print("The square of " + str(j) + " is " + str(square))
	
# While Loop

# The code in this loop will execute as long a given condition is true

print(" ")

ourCondition = True

while ourCondition == True:

	randomNumber = random.randint(0, 10)
	
	if randomNumber == 4:
		
		print("We got a 4! Exiting loop")
		
		ourCondition = False
	
	else:
	
		print("We got a " + str(randomNumber) + ". Looping again")
		
# Function

# Functions are bits of code that can be defined once and then be
# called, or used, again and again. If there's something that you
# need to do more than once, or a complicated procedure, it's best
# to put it in its own function

print(" ")

def sayHello(name):
	
	print("Hello, " + name + "!")
	
	
sayHello("Ron")
sayHello("Tom")



