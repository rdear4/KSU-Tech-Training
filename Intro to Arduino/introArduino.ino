
int LEDPin = 4;
int buttonPin = 8;


void setup() {

  pinMode(LEDPin, OUTPUT);

  //pinMode(buttonPin, INPUT);
  
}

void loop() {

//   digitalWrite(LEDPin, HIGH);
//
//   delay(100);
//
//   digitalWrite(LEDPin, LOW);
//
//   delay(100);

  if (digitalRead(buttonPin) == HIGH) {

    digitalWrite(LEDPin, HIGH);

  } else {

    digitalWrite(LEDPin, LOW);
    
  }
//
//  for (int i = 0; i < 255; i++ ) {
//
//    analogWrite(LEDPin, i);
//
//    delay(10);
//    
//  }
//
//  for (int i = 255; i >= 0; i--) {
//
//    analogWrite(LEDPin, i);
//
//    delay(10);
//    
//  }

  
}
