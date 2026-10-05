#citation: https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/
import cv2
import numpy as np
import mediapipe as mp

# Initialize mediapipe hand detection
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load class names manually if needed
classNames = ["Fist", "Thumbs Down", "Victory", "Thumbs Up", "Open Palm"]  # Example gestures

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read each frame
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)  # Flip horizontally for mirror effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for MediaPipe

    # Process the frame for hand detection
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)  # Draw landmarks

            # Extract landmark coordinates for gesture recognition
            landmarks = []
            for lm in handLms.landmark:
                h, w, _ = frame.shape
                landmarks.append((int(lm.x * w), int(lm.y * h)))

            # Example rule-based gesture detection (to be replaced with a better algorithm)
            if landmarks:
                fingers = [1 if landmarks[i][1] < landmarks[i - 2][1] else 0 for i in [8, 12, 16, 20]]
                thumb = 1 if landmarks[4][0] > landmarks[3][0] else 0
                total_fingers = fingers.count(1) + thumb

                gesture = f"Detected: {classNames[min(total_fingers, len(classNames) - 1)]}"
                cv2.putText(frame, gesture, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the output
    cv2.imshow("Hand Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
