#include <DHT.h>
/*
  HACE FALTA PONER UNA EXPLICACION AQUI JEJE
*/
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete
int tempPin = 7;
float temp = 0;
float celSum;
float humidity = 0;
float dhcel = 0;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  //Initialize dht sensor
  dht.begin();
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
    // Checar que no haya errores en los datos del sensor
    /*if (isnan(h) || isnan(t)) {
      Serial.println("Error obteniendo los datos del sensor DHT11");
      return;
    }*/

    temp = analogRead(tempPin);
    float mv = (temp/1024.0)*5000;
    float cel = mv/10;
    celSum += cel;

    if(i==9){
      // temperatura lm35
      cel = celSum/10;
      // humedad dht11
      humidity = dht.readHumidity();
      // temperatura dht11
      dhcel = dht.readTemperature();
      Serial.print(cel);
      Serial.print(",");
      Serial.print(humidity);
      Serial.print(",");
      Serial.print(dhcel);
      Serial.println();
    }
    delay(100);
}
  }
