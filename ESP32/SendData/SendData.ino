char data[] = "Hello World";

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.printf("%s%c",data,0x0D);
  delay(5000);
}
