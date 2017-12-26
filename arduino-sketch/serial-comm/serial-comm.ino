#include <DHT.h>
/*
  HACE FALTA PONER UNA EXPLICACION AQUI JEJE
*/


String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete
int tempPin = 7;
int humidityPin = 1;
float temp = 0;
float humidity = 0;
float celSum;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
      sendData();
    }
  }
}

void sendData() {
  for(int i=0; i < 10; i++){

    temp = analogRead(tempPin);
    float mv = (temp/1024.0)*5000;
    float cel = mv/10;
    celSum += cel;

    if(i==9){
      cel = celSum/10;
      Serial.print("Temp: ");
      Serial.print(cel);
      Serial.print(" C");
      Serial.println();
      celSum = 0;
    }
    delay(100);
}
  }
