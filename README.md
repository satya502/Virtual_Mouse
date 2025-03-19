<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Mouse Using Hand Tracking</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        code { background: #f4f4f4; padding: 5px; border-radius: 5px; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>Virtual Mouse Using Hand Tracking</h1>
    <p>This project implements a virtual mouse using OpenCV, MediaPipe, and PyAutoGUI. It enables users to control the mouse cursor using hand gestures, perform left clicks, and right clicks using finger movements.</p>
    
    <h2>Features</h2>
    <ul>
        <li>Tracks hand movements using MediaPipe's Hand Tracking solution.</li>
        <li>Moves the mouse cursor smoothly based on index finger position.</li>
        <li>Performs left-click when the thumb and index finger touch.</li>
        <li>Performs right-click when the index and middle fingers touch.</li>
        <li>Includes a cooldown mechanism to prevent accidental clicks.</li>
    </ul>
    
    <h2>Requirements</h2>
    <pre><code>pip install opencv-python mediapipe pyautogui numpy</code></pre>
    
    <h2>How to Run</h2>
    <ol>
        <li>Clone this repository:
            <pre><code>git clone https://github.com/your-username/your-repository.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd your-repository</code></pre>
        </li>
        <li>Run the script:
            <pre><code>python virtual_mouse.py</code></pre>
        </li>
    </ol>
    
    <h2>Usage</h2>
    <ul>
        <li>Move your index finger to control the cursor.</li>
        <li>Pinch your thumb and index finger together to perform a left-click.</li>
        <li>Pinch your index and middle fingers together to perform a right-click.</li>
        <li>Press <code>q</code> to exit the program.</li>
    </ul>
    
    <h2>Troubleshooting</h2>
    <ul>
        <li>Ensure your webcam is functioning properly.</li>
        <li>Adjust the detection confidence if hand tracking is inaccurate.</li>
        <li>Run the script in a well-lit environment for better detection.</li>
    </ul>
    
    <h2>License</h2>
    <p>This project is open-source and available under the MIT License.</p>
    
    <h2>Author</h2>
    <p>Your Name</p>
    
    <p>Feel free to contribute or suggest improvements!</p>
</body>
</html>

