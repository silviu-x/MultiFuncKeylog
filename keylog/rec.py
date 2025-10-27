import dxcam
import cv2
import numpy as np
import pyautogui  # add this for fallback

# Create camera instance
camera = dxcam.create()

# Get screen size safely
try:
    screen_width, screen_height = camera.target.width, camera.target.height
except AttributeError:
    screen_width, screen_height = pyautogui.size()

# Define video writer for MP4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
out = cv2.VideoWriter('screen_record.mp4', fourcc, 30.0, (screen_width, screen_height))

# Start capturing
camera.start()

try:
    while True:
        frame = camera.get_latest_frame()
        if frame is not None:
            # Convert RGB (dxcam) to BGR (OpenCV)
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame_bgr)
except KeyboardInterrupt:
    print("Stopping recording...")

camera.stop()
out.release()
