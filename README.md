# Virtual Mouse Using Hand Tracking

This project implements a virtual mouse using OpenCV, MediaPipe, and PyAutoGUI. It enables users to control the mouse cursor using hand gestures, perform left clicks, and right clicks using finger movements.

## Features
- Tracks hand movements using MediaPipe's Hand Tracking solution.
- Moves the mouse cursor smoothly based on index finger position.
- Performs left-click when the thumb and index finger touch.
- Performs right-click when the index and middle fingers touch.
- Includes a cooldown mechanism to prevent accidental clicks.

## Requirements
```html
pip install opencv-python mediapipe pyautogui numpy
```

## How to Run
1. Clone this repository:
```html
git clone https://github.com/satya502/Virtual_Mouse/tree/main
```
2. Navigate to the project directory:
```html
cd Virtual_Mouse
```
3. Run the script:
```html
python virtual_mouse.py
```

## Usage
- Move your index finger to control the cursor.
- Pinch your thumb and index finger together to perform a left-click.
- Pinch your index and middle fingers together to perform a right-click.
- Press `q` to exit the program.

## Troubleshooting
- Ensure your webcam is functioning properly.
- Adjust the detection confidence if hand tracking is inaccurate.
- Run the script in a well-lit environment for better detection.


