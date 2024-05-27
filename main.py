import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Mediapipe el izleme modelini başlat
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Webcam'i başlat
cap = cv2.VideoCapture(0)

# Ekran boyutunu al
screen_width, screen_height = pyautogui.size()

# Fare tıklama durumu kontrolü
scrolling = False

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Aynalama
    h, w, c = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Parmağın uç noktalarını al
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Ekran boyutuna göre koordinatları dönüştür
            thumb_x = int(thumb_tip.x * w)
            thumb_y = int(thumb_tip.y * h)
            index_x = int(index_tip.x * w)
            index_y = int(index_tip.y * h)
            middle_x = int(middle_tip.x * w)
            middle_y = int(middle_tip.y * h)

            # İşaret parmağı ve baş parmak arasındaki mesafeyi hesapla
            distance_thumb_index = np.hypot(index_x - thumb_x, index_y - thumb_y)
            # İşaret parmağı ve orta parmak arasındaki mesafeyi hesapla
            distance_index_middle = np.hypot(index_x - middle_x, index_y - middle_y)

            # Mouse hareketi işaret ve baş parmak belirli bir mesafedeyken etkin olsun
            if 30 <= distance_thumb_index < 60:
                # Mouse hareketi
                screen_x = screen_width / w * index_x
                screen_y = screen_height / h * index_y
                pyautogui.moveTo(screen_x, screen_y)

            # İşaret parmağı ve baş parmak arasındaki mesafe küçükse sol tıklama
            elif distance_thumb_index < 30:
                pyautogui.click()
                pyautogui.sleep(0.2)  # Çift tıklamayı önlemek için bekle

            # İşaret ve orta parmak arasındaki mesafe küçükse sağ tıklama
            elif distance_index_middle < 30:
                pyautogui.rightClick()
                pyautogui.sleep(0.2)  # Çift tıklamayı önlemek için bekle
    
    cv2.imshow("Sanal Mouse", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
