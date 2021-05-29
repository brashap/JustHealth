/*
 * Project SerialSend
 * Description: Send data over Serial port
 * Author: Brian Rashap
 * Date: 27-May-2021
 */


uint8_t data;
char data2[] = "8E6FD304-B90D-9726-FA38-1E9D3646B713,8E6FD304-25B3-6056-3069-9B41C81981BE,8E6FD304-25B3-CEBC-1B7E-444B69A4A92C,8E6FD304-25B3-CEBC-70EA-823B91804DDA,1,1,00:25:10,46,2.39,20.96,2";

void setup() {
  Serial1.begin(115200);
}

void loop() {
  data = random(0x41,0x5B);
  /*Serial1.write(data);
  Particle.publish(String(data));
  */
  Serial1.printf("%s",data2);
  Particle.publish(String(data2));
  Particle.publish(String(sizeof(data2)));

  delay(5000);
}