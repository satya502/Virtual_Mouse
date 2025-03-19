import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize hand tracking
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

# Get screen size
screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)

# Smooth cursor movement
prev_x, prev_y = 0, 0
smooth_factor = 5  # Increased smoothing for more fluid movement 
click_cooldown = time.time()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)  # Mirror effect
    h, w, c = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            index_finger_tip = landmarks[8]  # Index finger tip
            thumb_tip = landmarks[4]  # Thumb tip
            middle_finger_tip = landmarks[12]  # Middle finger tip
            wrist = landmarks[0]  # Wrist for distance calculation

            # Convert coordinates
            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            screen_x, screen_y = int(index_finger_tip.x * screen_w), int(index_finger_tip.y * screen_h)

            # Enhanced smooth cursor movement
            new_x = prev_x + (screen_x - prev_x) / smooth_factor
            new_y = prev_y + (screen_y - prev_y) / smooth_factor

            pyautogui.moveTo(new_x, new_y, duration=0.05)  # Added slight duration for extra smoothness
            prev_x, prev_y = new_x, new_y

            # Calculate hand distance from camera using wrist position
            hand_depth = wrist.z  # Z value indicates distance from camera

            # Left Click with cooldown
            thumb_index_dist = np.linalg.norm(
                np.array([thumb_tip.x, thumb_tip.y]) - np.array([index_finger_tip.x, index_finger_tip.y])
            )
            if thumb_index_dist < 0.05 and time.time() - click_cooldown > 0.5:
                pyautogui.click()
                click_cooldown = time.time()
                cv2.putText(frame, 'Left Click', (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Right Click with additional conditions to avoid false triggers
            index_middle_dist = np.linalg.norm(
                np.array([index_finger_tip.x, index_finger_tip.y]) - np.array([middle_finger_tip.x, middle_finger_tip.y])
            )
            if index_middle_dist < 0.05 and time.time() - click_cooldown > 0.5 and hand_depth > -0.2:
                pyautogui.rightClick()
                click_cooldown = time.time()
                cv2.putText(frame, 'Right Click', (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



