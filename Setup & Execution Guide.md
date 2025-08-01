Hardware Connections (According to the Code)
Pan Servo Motor

Signal wire → Arduino Digital Pin 9

Power (Red) → 5V

Ground (Black or Brown) → GND

Tilt Servo Motor

Signal wire → Arduino Digital Pin 10

Power (Red) → 5V

Ground (Black or Brown) → GND

I2C LCD Display

SDA → Arduino Analog Pin A4

SCL → Arduino Analog Pin A5

VCC → 5V

GND → GND

Arduino to Computer

Connect via USB cable (for serial communication)

Python Environment Setup
Make sure Python 3.x is installed.
Note: Some libraries like Mediapipe may not work properly with Python 3.12+. It's recommended to use versions between 3.8 and 3.11.

Install the required libraries:

pip install pyserial mediapipe opencv-python
Steps to Run the Python Script (via CMD):

Navigate to the desktop (so Python can find your script easily):
cd "%USERPROFILE%\Desktop"

(Optional)Activate your virtual environment:
mpenv\Scripts\activate

Run the Python script (change the filename if necessary):
python eltakip.py




Donanım Bağlantıları (Koda Göre)
Pan Servo Motor: Arduino dijital pin 9’a bağlanır.

Servo sinyal pini → Arduino D9

Güç (Kırmızı) → 5V

Toprak (Siyah veya kahverengi) → GND

Tilt Servo Motor: Arduino dijital pin 10’a bağlanır.

Servo sinyal pini → Arduino D10

Güç (Kırmızı) → 5V

Toprak (Siyah veya kahverengi) → GND

I2C LCD Ekran:

SDA → Arduino analog pin A4

SCL → Arduino analog pin A5

Güç (VCC) → 5V

Toprak (GND) → GND

Arduino - Bilgisayar:

USB kablosu ile bağlanır (seri iletişim için)


Python Ortamının Hazırlanması
Python 3.x kurulu olduğundan emin olun (Not: Mediapipe gibi bazı kütüphaneler Python 3.12+ sürümlerinde çalışmayabilir, bu yüzden 3.8 - 3.11 sürümleri önerilir.) :D 

Gerekli kütüphaneleri yükleyin:
pip install pyserial mediapipe opencv-python

kodları cmd üzerinden işledim cmdye sırayla yazarken bunları yaptım
1- cd "%USERPROFILE%\Desktop" (olurda .py dosyanızı bulmazsa,masaüstünün tamamını görür :D)
2-mpenv\Scripts\activate (Sanal ortam varsa aktif eder)
3-python eltakip.py (son olarak python dosyasını çalıştırmak, ismi kendi projenize göre değiştirin.) 
