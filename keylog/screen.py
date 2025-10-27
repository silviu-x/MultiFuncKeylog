import dxcam
from PIL import Image
import os
import time
from datetime import datetime

# Create camera object
camera = dxcam.create()  # returns a DXCamera instance on primary monitor

# Folder to save screenshots (same folder as script)
script_folder = os.path.dirname(os.path.abspath(__file__))

while True:
    # Grab a frame
    frame = camera.grab()
    
    # Convert to PIL Image
    img = Image.fromarray(frame)
    
    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(script_folder, f"screenshot_{timestamp}.png")
    
    # Save the image
    img.save(file_path)
    
    # Wait 60 seconds
    time.sleep(60)