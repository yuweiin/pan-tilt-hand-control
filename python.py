import cv2
import mediapipe as mp
import serial
import time

# Arduino seri portu (COM3 yerine kendi portunu yaz)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Arduino’nun hazır olması için bekleme

# MediaPipe ayarları
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Kamera başlat
cap = cv2.VideoCapture(0)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Görüntüyü çevir ve RGB’ye dönüştür
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Elleri işle
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # İşaret parmağı ucu (landmark 8)
                x = hand_landmarks.landmark[8].x  # 0.0 - 1.0 arası
                y = hand_landmarks.landmark[8].y

                # 0–1 arası değerleri 0–180'e çevir
                tilt_angle = int(x * 180)
                pan_angle = int(y * 180)

                # Arduino’ya komut gönder (örneğin: "90 60\n")
                command = f"{pan_angle} {tilt_angle}\n"
                arduino.write(command.encode('utf-8'))
                time.sleep(0.02)  # Veri akışını yavaşlat

                # Görsel olarak el çizimi yap
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Görüntüyü göster
        cv2.imshow('El Takibi', frame)

        # ESC tuşu ile çık
        if cv2.waitKey(5) & 0xFF == 27:
            break

except KeyboardInterrupt:
    print("Çıkılıyor...")

finally:
    cap.release()
    arduino.close()
    cv2.destroyAllWindows()
