int LEDPin = 4;
int buttonPin = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(LEDPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  
}

void loop() {

 int pinValue = digitalRead(buttonPin);

 if (pinValue == LOW) {
    digitalWrite(LEDPin, HIGH);
 } else {
    digitalWrite(LEDPin, LOW);
 }
  
}
