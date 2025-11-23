Pan-Tilt Object Tracking System (Computer Vision & Arduino)

English Description

This project implements a real-time computer vision-based control system for a 2-axis Pan-Tilt servo mechanism using Python (OpenCV/MediaPipe) and Arduino.

The system captures video input, processes it to track hand gestures or face coordinates, and sends angle calculations to the Arduino microcontroller via serial communication. This creates a closed-loop control system where hardware responds to software-defined targets instantly.

🚀 Key Features

Real-Time Tracking: High-performance object/hand tracking using MediaPipe & OpenCV.

Serial Communication: Seamless data transfer between Python scripts and Arduino firmware.

2-Axis Control: Precise control of Pan (X-axis) and Tilt (Y-axis) servo motors.

User Feedback: Integrated 16x2 I2C LCD for real-time system status and coordinate display.

Modular Architecture: Easily expandable for different sensors (e.g., Lidar, Ultrasonic).

🛠 Hardware Requirements

Microcontroller: Arduino Uno (or compatible AVR/ESP boards).

Actuators: 2x SG90 or MG996R Servo Motors.

Display: 16x2 LCD with I2C Interface.

Power: External 5V Power Supply (Recommended for servos).

Connection: USB Cable (Serial Com).

💻 Software Dependencies

To run the Python script, install the required libraries:

pip install opencv-python
pip install mediapipe
pip install pyserial


Türkçe Açıklama

Bu proje, Python (OpenCV/MediaPipe) ve Arduino kullanılarak geliştirilmiş, görüntü işleme tabanlı bir 2 eksenli Pan-Tilt kontrol sistemidir.

Sistem, kamera görüntüsünü işleyerek el hareketlerini veya yüz koordinatlarını tespit eder. Hesaplanan açı verileri, seri haberleşme (Serial Communication) üzerinden Arduino'ya iletilir. Bu sayede donanım, yazılım tarafından belirlenen hedefe gerçek zamanlı olarak odaklanır.

🚀 Temel Özellikler

Gerçek Zamanlı Takip: MediaPipe ve OpenCV kullanarak düşük gecikmeli nesne/el takibi.

Seri Haberleşme: Python ve Arduino arasında optimize edilmiş veri akışı.

2 Eksenli Kontrol: Pan (Yatay) ve Tilt (Dikey) servo motorlarının hassas kontrolü.

Geri Bildirim Sistemi: I2C LCD ekran üzerinden anlık koordinat ve durum bilgisi.

Modüler Yapı: Mesafe sensörü veya lazer modülü gibi eklemeler için uygun altyapı.

🛠 Donanım Gereksinimleri

Mikrodenetleyici: Arduino Uno (veya uyumlu kartlar).

Eyleyiciler: 2 adet Servo Motor (Pan ve Tilt eksenleri için).

Ekran: I2C arayüzlü 16x2 LCD Ekran.

Güç: Servolar için harici 5V güç kaynağı (Önerilir).

🤝 Contribution / Katkı

This project is open to development. If you want to improve the code or add new features (like PID control), feel free to submit a Pull Request.

Bu proje geliştirmeye açıktır. PID kontrolü eklemek veya performansı artırmak isterseniz Pull Request gönderebilirsiniz.

Developed by Esma Demirhan
