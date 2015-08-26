#include "DHT.h"

#define DHTPIN 5     // what pin DHT is connected to
#define LightPIN 2   // what pin photosensor is connected
#define MoisturePIN 4   // what pin photosensor is connected

#define DHTTYPE DHT11   // DHT 11 
DHT dht(DHTPIN, DHTTYPE);
int show = 0;
void setup() {
  Serial.begin(9600); 
  //Serial.println("DHTxx test!");

  dht.begin();
}

void loop() {

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Read photosensor
  float l = analogRead(LightPIN);

  // Read moisture sensor
  float m = analogRead(MoisturePIN);

  // Compute heat index
  // Must send in temp in Fahrenheit!
  float hi = dht.computeHeatIndex(f, h);
  if(show)
  {
    Serial.print("Humidity: "); 
    Serial.print(h);
    Serial.print(" %\t");
    Serial.print("Temperature: "); 
    Serial.print(t);
    Serial.print(" *C ");
    Serial.print(f);
    Serial.print(" *F\t");
    Serial.print("Heat index: ");
    Serial.print(hi);
    Serial.print(" *F\t");
    Serial.print("Light: ");
    Serial.print(l);
    Serial.print("\t");
    Serial.print("Moisture: ");
    Serial.println(m);
  }
  else
  {
    // Temperature
    Serial.print(t);
    Serial.print(";");

    // Humidity
    Serial.print(h);
    Serial.print(";");

    // Light
    Serial.print(l);
    Serial.print(";");

    // Moisture
    Serial.print(m);
    Serial.println(";");

  }

  // Wait 5 minutes between measurements.
  delay(300000);
}

