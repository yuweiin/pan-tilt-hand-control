#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

Servo panServo;
Servo tiltServo;

LiquidCrystal_I2C lcd(0x27, 16, 2); // LCD adresin farklıysa 0x3F olabilir

void setup() {
  Serial.begin(9600);
  panServo.attach(9);   // Pan için servo pini
  tiltServo.attach(10); // Tilt için servo pini

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Pan-Tilt Basliyor");
  delay(1500);
  lcd.clear();
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int spaceIndex = data.indexOf(' ');
    if (spaceIndex != -1) {
      int pan = data.substring(0, spaceIndex).toInt();
      int tilt = data.substring(spaceIndex + 1).toInt();

      // Servo açılarını ayarla
      panServo.write(pan);
      tiltServo.write(tilt);

      // LCD'ye yazdır
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Pan: ");
      lcd.print(pan);
      lcd.setCursor(0, 1);
      lcd.print("Tilt: ");
      lcd.print(tilt);
    }
  }
}
