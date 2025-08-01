English:

This project implements a hand gesture-based control system for a pan-tilt servo mechanism using Arduino and Python. The Arduino reads servo angle commands via serial communication and drives two servo motors for pan and tilt movement. Python performs real-time hand tracking (e.g., with MediaPipe or OpenCV) and sends angle commands to the Arduino over the serial port.

Key Features:

Real-time serial communication between Python and Arduino

Servo control for pan and tilt axes

Feedback display via I2C 16x2 LCD screen

Modular and extensible design

Materials Used:

Arduino Uno (or compatible microcontroller)

2x Servo Motors (for pan and tilt movement)

I2C interface 16x2 LCD display

USB cable (for Arduino-Python communication)

Jumper wires and breadboard (for circuit connections)

Python 3.x environment and required libraries (pyserial, mediapipe/opencv, etc.)

This project presents a basic Pan-Tilt hand control system and is open to further development.
If you’ve integrated it into your own projects or built upon it, I’d be glad to see your work 

I openly welcome any suggestions, improvements, or corrections. My goal is to enhance this project and take it to a more advanced and refined level. :)







Türkçe:

Bu proje, Arduino ve Python kullanarak el hareketleriyle pan-tilt servo mekanizmasını kontrol eden bir sistemdir. Arduino, seri haberleşme ile gelen servo açı komutlarını okuyarak pan ve tilt için iki servo motoru sürer. Python ise gerçek zamanlı el takibi (MediaPipe veya OpenCV gibi) yapar ve açılar şeklinde komutları Arduino’ya seri port üzerinden gönderir.

Temel özellikler:

Python ve Arduino arasında gerçek zamanlı seri iletişim

Pan ve tilt eksenleri için servo kontrolü

I2C üzerinden LCD geri bildirim ekranı

Modüler ve genişletilebilir yapı

Kullanılan Malzemeler:

Arduino Uno (veya uyumlu bir mikrodenetleyici)

2 adet Servo Motor (Pan ve Tilt hareketleri için)

I2C arayüzlü 16x2 LCD ekran

USB kablosu (Arduino-Python iletişimi için)

Bağlantı kabloları ve breadboard (devre bağlantıları için)

Python 3.x ortamı ve ilgili kütüphaneler (pyserial, mediapipe/opencv vb.)

-Malzemeleri robotistan’dan aldım. İsterseniz projeye mesafe sensörü, buzzer ve LED gibi bileşenler ekleyerek sistemi daha da geliştirebilirsiniz :) 


Bu proje temel bir Pan-Tilt el kontrol sistemi sunmaktadır ve geliştirmeye açıktır.
Eğer projeyi kendi çalışmalarınıza entegre ettiyseniz ya da üzerine yeni özellikler eklediyseniz, lütfen benimle paylaşın 

Her türlü öneri, katkı veya düzeltme taleplerine açığım. Amacım bu projeyi daha üst seviyelere taşımak ve olabildiğince nitelikli hale getirmek. :))
