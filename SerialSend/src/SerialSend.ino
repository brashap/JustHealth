/*
 * Project SerialSend
 * Description: Send data over Serial port
 * Author: Brian Rashap
 * Date: 27-May-2021
 */


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