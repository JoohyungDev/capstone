#include <Servo.h>

int incomingByte;
Servo servo1;
Servo servo2;

int pos = 0;

void setup() {
  servo1.attach(9);
  servo2.attach(10);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'H') {
      for (pos = 0; pos <= 180; pos += 1) {
        servo1.write(pos);
        delay(15);
      }
      delay(2000);
      for (pos = 180; pos >= 0; pos -= 1) {
        servo1.write(pos);
        delay(15);
      }
    } else if (incomingByte == 'L') {
      // for (pos = 180; pos >= 0; pos -= 1) {
      //   servo1.write(pos);
      //   delay(15);
      // }
      delay(2000);
      // for (pos = 0; pos <= 180; pos += 1) {
      //   servo1.write(pos);
      //   delay(15);
      // }
    }
  }
}
