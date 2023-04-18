#include "BLEDevice.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  BLEDevice::getScan()->start(5);

  if(BLEDevice.haveRSSI && BLEDevice.getName() == "AkselBLE"){
    Serial.println(BLEDevice.getRSSI());
  }
}