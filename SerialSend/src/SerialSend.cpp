/******************************************************/
//       THIS IS A GENERATED FILE - DO NOT EDIT       //
/******************************************************/

#include "Particle.h"
#line 1 "c:/Users/IoT_Instructor/Documents/JustHealth/SerialSend/src/SerialSend.ino"
/*
 * Project SerialSend
 * Description: Send data over Serial port
 * Author: Brian Rashap
 * Date: 27-May-2021
 */


void setup();
void loop();
#line 9 "c:/Users/IoT_Instructor/Documents/JustHealth/SerialSend/src/SerialSend.ino"
uint8_t data;

void setup() {
  Serial1.begin(115200);
}

void loop() {
  data = random(0x41,0x5B);
  Serial1.write(data);
  Particle.publish(String(data));
  delay(5000);
}