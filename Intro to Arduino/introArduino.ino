
int LEDPin = 4;
int buttonPin = 8;


void setup() {

  pinMode(LEDPin, OUTPUT);

  pinMode(buttonPin, INPUT);
  
}

void loop() {
  
  //Part 1 of the workshop
  digitalWrite(LEDPin, HIGH);

  delay(100);

  digitalWrite(LEDPin, LOW);

  delay(100);
  
  //Part 2 of the workshop
  if (digitalRead(buttonPin) == HIGH) {

    digitalWrite(LEDPin, HIGH);

  } else {

    digitalWrite(LEDPin, LOW);
    
  }

  
}
