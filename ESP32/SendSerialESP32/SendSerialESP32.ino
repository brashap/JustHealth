/*
 * Project SerialSend
 * Description: Send data over Serial port
 * Author: Brian Rashap
 * Date: 27-May-2021
 */
​
//char data[] = "8E6FD304-B90D-9726-FA38-1E9D3646B713,8E6FD304-25B3-6056-3069-9B41C81981BE,8E6FD304-25B3-CEBC-1B7E-444B69A4A92C,8E6FD304-25B3-CEBC-70EA-823B91804DDA,1,1,00:25:10,46,2.39,20.96,2";
​uint8_t data = 0x41;
void setup() {
  Serial.begin(115200);
}
​
void loop() {
  Serial.print(data);
  //Serial.print(0x0D);
  delay(5000);
}
