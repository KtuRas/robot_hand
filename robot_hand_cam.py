import cv2
import mediapipe as mp
import serial
import time

try:
  ser=serial.Serial('/dev/ttyUSB0',115200)
except:
  ser=serial.Serial('COM6',115200)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

x_diff = 0


cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.9,
    min_tracking_confidence=0.9) as hands:
  direction = -1  
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      
      continue


    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    image.flags.writeable = False
    results = hands.process(image)

    
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    fingers = [0, 0, 0, 0, 0, 1]
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        
        landmarks = hand_landmarks.landmark

        
        x5, y5, z5 = landmarks[5].x, landmarks[5].y, landmarks[5].z
        x17, y17, z17 = landmarks[17].x, landmarks[17].y, landmarks[17].z

        if x5 < x17 and z5 < z17:
          fingers[5] = 0
        elif x5 < x17 and z5 > z17:
          fingers[5] = 2
        else:
          fingers[5] = 1

        x, y = hand_landmarks.landmark[1].x, hand_landmarks.landmark[1].y
        x1, y1 = hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y
        x2, y2 = hand_landmarks.landmark[5].x, hand_landmarks.landmark[5].y
        x3, y3 = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y
        x4, y4 = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y
        x5, y5 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y
        x6, y6 = hand_landmarks.landmark[13].x, hand_landmarks.landmark[13].y
        x7, y7 = hand_landmarks.landmark[16].x, hand_landmarks.landmark[16].y
        x8, y8 = hand_landmarks.landmark[17].x, hand_landmarks.landmark[17].y
        x9, y9 = hand_landmarks.landmark[20].x, hand_landmarks.landmark[20].y
        
        x_diff = x8 - x2
        if x_diff > 0:
            fingers[0] = 1 if x1 > x2 else 0
            fingers[1] = 1 if y3 > y2 else 0
            fingers[2] = 1 if y5 > y4 else 0
            fingers[3] = 1 if y7 > y6 else 0
            fingers[4] = 1 if y9 > y8 else 0
        else:
            fingers[4] = 1 if y9 > y8 else 0
            fingers[3] = 1 if y7 > y6 else 0
            fingers[2] = 1 if y5 > y4 else 0
            fingers[1] = 1 if y3 > y2 else 0
            fingers[0] = 1 if x2 > x1 else 0

        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    
    mystring = "#".join(str(element) for element in fingers)
    print(mystring)
    ser.write(mystring.encode())

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(1) ==ord('q'):
      break

    time.sleep(0.005)

cap.release()
cv2.destroyAllWindows()
