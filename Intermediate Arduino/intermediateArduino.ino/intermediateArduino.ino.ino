#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

//Define the pins for the LEDs and the button
int LEDPin = 2;
int buttonPin = 0;

//setup the variables for the program
bool buttonIsPressed = false;
int programMode = 0;

//Define the total number of modes
int totalNumberOfProgramModes = 5;

//Setup the neopixel strip
Adafruit_NeoPixel stick = Adafruit_NeoPixel(8, LEDPin, NEO_GRB + NEO_KHZ800);

void setup() {
  
  //setup the pins on the arduino
  pinMode(buttonPin, INPUT);
  
  //set the pull-up resistor for the button pin
  digitalWrite(buttonPin, HIGH);
  
  //Get the LED stick ready to use
  stick.begin();  //Initialize the stick
  stick.show();   //Call show to clear the LEDs
  
  
  //programMode starts out being equal to 0
  //Turn on the 1st LED. Remember to start counting from 0
  stick.setPixelColor(programMode, stick.Color(0, 10, 50));
  stick.show();

}

void loop() {
  
  //We start out every loop checking to see if the button is being pressed.
  //We don't want anything to happen if you hold the button downl; only if
  //you press the button, release it and then press it again.

  //Check to see if the button is pressed
  if (buttonIsPressed == false) {

    //If the button was not being pressed, check to see if it is being pressed now.
    //Remember that a value of LOW means the button is being pressed.
    if (digitalRead(buttonPin) == LOW) {

      //If the button is being pressed, immediately set the buttonIsPressed vaiable to 'true'
      buttonIsPressed = true;

      //Every time the button is pressed, increment the programMode by one
      programMode = programMode + 1;

      //If the current programMode value is greater than the value of the totalNumberOfProgramModes
      //reset it back to zero.
      
      if (programMode >= totalNumberOfProgramModes) {
      
        programMode = 0;
      
      }
      
      //Before we update the LEDs to show the correct mode
      //we have to clear all the LEDs out
      clearLEDStick();

      
      stick.setPixelColor(programMode, stick.Color(0, 10, 50));
      stick.show();
      delay(100);
      
    }
    
  } else {
    
      if (digitalRead(buttonPin) == HIGH) {
      
        buttonIsPressed = false;
      
      }
    
  }

  //If you want something different to happen for the differnt modes you can do something like this
  //Remember to uncomment out the following lines if you want to use them.
  //To uncomment them out, simply remove the '//' before each line.
//  switch(programMode) {
//    case: 0 {
//      mode0();
//      break;
//    case 1:
//      mode1();
//      break;
//    case 2:
//      mode2()
//      break;
//    case 3:
//      mode3();
//      break;
//    case 4:
//      mode4();
//      break;
//    }
//  }
  
}

void mode0() {

  //Do something for mode0
}

void mode1() {

  //Do something for mode1
}

void mode2() {

  //Do something for mode2
}

void mode3() {

  //Do something for mode3
}

void mode4() {

  //Do something for mode4
}

void clearLEDStick() {
  
  for (int i = 0; i < 8; i++) {
    
    stick.setPixelColor(i, stick.Color(0, 0, 0));
    
  }
  
  stick.show();
  
}
