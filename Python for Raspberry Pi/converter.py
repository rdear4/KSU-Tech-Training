###################################################################
#
#	Title 		: Converter
#	Author		: Ron Dear
#	Date		: 9/12/2017
#	Description	: This program will take the input from the user
#				  and convert it to various other measurement units
#
###################################################################

def main():

	print("")
	print("What would you like to convert?")
	print("")
	print("1 Convert Celsius to Fahrenheit")
	print("2 Convert Fahrenheit to Celsius")
	print("3 Convert miles to kilometers")
	print("4 Convert kilometers to miles")
	print("5 Quit")
	print("")
	print("")
	
	selection = raw_input("Please enter your selection: ")
	
	if (selection == "1"):
		print("")
		celsiusToFahrenheit()
	
	if (selection == "2"):
		print("")
		fahrenheitToCelsius()
		
	if (selection == "3"):
		print("")
		milesToKilometers()
		
	if (selection == "4"):
		print("")
		kilometersToMiles()
	
	if (selection == "5"):
		print("")
		print("Goodbye!")
		
def celsiusToFahrenheit():
	
	tempInC = raw_input("What is the temperature in celsius? ")
	
	print("")
	
	tempInF = ( float(tempInC) * ( 9.0/5.0 ) ) + 32
	
	print("That temperature is " + str(tempInF) + " degrees fahrenheit")
	
	main()
	
def fahrenheitToCelsius():
	
	tempInF = raw_input("What is the temperature in fahrenheit? ")
	
	print("")
	
	tempInC = ( float(tempInF) - 32.0 ) * ( 5.0/9.0 )
	
	print("That temperature is " + str(tempInC) + " degrees celsius")
	
	main()

def milesToKilometers():
	
	distanceInMiles = raw_input("What is the distance in miles? ")
	
	print("")
	
	distanceInKilometers = float(distanceInMiles) * 1.609
	
	print("The distance in kilometers is " + str(distanceInKilometers))
	
	main()

def kilometersToMiles():
	
	distanceInKilometers = raw_input("What is the distance in kilometers? ")
	
	print("")
	
	distanceInMiles = float(distanceInKilometers) / 1.609
	
	print("The distance in miles is " + str(distanceInMiles))	
	
	main()

if __name__ == "__main__":

	main()