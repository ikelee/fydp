#include "ADXL375.h"

ADXL375 accel;

void setup() {
  Serial.begin(9600);
  while(!Serial.available());
  Serial.println("test");

}

void loop() {
  // put your main code here, to run repeatedly:

}
