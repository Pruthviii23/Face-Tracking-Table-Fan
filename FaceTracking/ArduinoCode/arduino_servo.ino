#include <Servo.h>

Servo servoX;  // Horizontal (Pan)
Servo servoY;  // Vertical (Tilt)

int xAngle = 90;
int yAngle = 90;

void setup() {
  Serial.begin(9600);
  servoX.attach(9);   // Pan servo connected to digital pin 9
  servoY.attach(10);  // Tilt servo connected to digital pin 10

  servoX.write(xAngle);
  servoY.write(yAngle);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');

    if (commaIndex > 0) {
      // Parse angles from string
      xAngle = data.substring(0, commaIndex).toInt();
      yAngle = data.substring(commaIndex + 1).toInt();

      // Constrain to servo limits
      xAngle = constrain(xAngle, 0, 180);
      yAngle = constrain(yAngle, 0, 180);

      // Move servos
      servoX.write(xAngle);
      servoY.write(yAngle);

      // Debug output
      Serial.print("X Angle: ");
      Serial.print(xAngle);
      Serial.print(", Y Angle: ");
      Serial.println(yAngle);
    }
  }
}
